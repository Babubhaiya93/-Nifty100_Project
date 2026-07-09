"""
Portfolio Recommendation Engine
Sprint 3 - Day 21
"""

import sqlite3
import pandas as pd


def load_data(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        fr.company_id,
        s.broad_sector,
        fr.return_on_equity_pct,
        fr.net_profit_margin_pct,
        fr.asset_turnover,
        fr.debt_to_equity,
        fr.free_cash_flow_cr
    FROM financial_ratios fr
    LEFT JOIN sectors s
    ON fr.company_id = s.company_id
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def build_portfolio(df):

    score = (
        df["return_on_equity_pct"].fillna(0)
        + df["net_profit_margin_pct"].fillna(0)
        + df["asset_turnover"].fillna(0) * 20
        + df["free_cash_flow_cr"].fillna(0) / 100
        - df["debt_to_equity"].fillna(0) * 10
    )

    df["portfolio_score"] = score

    ranking = (
        df.groupby("company_id")["portfolio_score"]
        .mean()
        .reset_index()
    )

    ranking = ranking.sort_values(
        by="portfolio_score",
        ascending=False
    )

    return ranking


def export_portfolio(df):

    output_file = "output/portfolio_recommendation.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("PORTFOLIO GENERATED")
    print("=" * 60)
    print("Output :", output_file)
    print("Companies :", len(df))


def generate_portfolio(db_path):

    df = load_data(db_path)

    portfolio = build_portfolio(df)

    export_portfolio(portfolio)

    return portfolio