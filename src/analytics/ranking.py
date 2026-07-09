"""
Company Ranking Engine
Sprint 3 - Day 20
"""

import sqlite3
import pandas as pd


def load_data(db_path):
    """
    Load financial ratios from SQLite.
    """

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        fr.*,
        s.broad_sector
    FROM financial_ratios fr
    LEFT JOIN sectors s
    ON fr.company_id = s.company_id
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def normalize(series):
    """
    Normalize values between 0 and 100.
    """

    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series(50, index=series.index)

    return ((series - minimum) / (maximum - minimum)) * 100


def calculate_score(df):

    score = pd.Series(0, index=df.index)

    metrics = [
        "return_on_equity_pct",
        "net_profit_margin_pct",
        "asset_turnover",
        "interest_coverage",
        "free_cash_flow_cr"
    ]

    for metric in metrics:

        if metric in df.columns:

            score += normalize(
                df[metric].fillna(0)
            )

    df["overall_score"] = score

    return df


def rank_companies(df):

    df = calculate_score(df)

    ranking = (
        df.groupby("company_id", as_index=False)["overall_score"]
        .mean()
        .sort_values(
            by="overall_score",
            ascending=False
        )
    )

    ranking["rank"] = range(
        1,
        len(ranking) + 1
    )

    return ranking


def export_ranking(df):

    output_file = "output/company_ranking.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("COMPANY RANKING GENERATED")
    print("=" * 60)
    print("Output :", output_file)
    print("Companies :", len(df))


def generate_ranking(db_path):

    df = load_data(db_path)

    ranking = rank_companies(df)

    export_ranking(ranking)

    return ranking


if __name__ == "__main__":

    ranking = generate_ranking("nifty100.db")

    print(ranking.head(20))