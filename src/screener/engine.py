"""
Stock Screener Engine
Sprint 3 - Day 15
"""

import sqlite3
import pandas as pd

from src.screener.score import calculate_composite_score

def load_financial_data(db_path):
    """
    Load financial ratios + sector information from SQLite database.
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


def apply_filters(df, filters):

    # ROE Filter
    if (
        "return_on_equity_pct" in df.columns
        and "roe_min" in filters
    ):
        df = df[
            df["return_on_equity_pct"] >=
            filters["roe_min"]
        ]

    # Debt-to-Equity Filter
    # Financial companies are automatically allowed
    if (
        "debt_to_equity" in df.columns
        and "broad_sector" in df.columns
        and "debt_to_equity_max" in filters
    ):
        df = df[
            (df["broad_sector"] == "Financials") |
            (df["debt_to_equity"] <= filters["debt_to_equity_max"])
        ]

    # Free Cash Flow Filter
    if (
        "free_cash_flow_cr" in df.columns
        and "fcf_min" in filters
    ):
        df = df[
            df["free_cash_flow_cr"] >=
            filters["fcf_min"]
        ]

    # Revenue CAGR Filter (only if available)
    if (
        "revenue_cagr_5yr" in df.columns
        and "revenue_cagr_min" in filters
    ):
        df = df[
            df["revenue_cagr_5yr"] >=
            filters["revenue_cagr_min"]
        ]

    return df


def add_composite_score(df):

    score = 0

    if "return_on_equity_pct" in df.columns:
        score += df["return_on_equity_pct"].fillna(0)

    if "return_on_capital_employed_pct" in df.columns:
        score += df["return_on_capital_employed_pct"].fillna(0)

    if "net_profit_margin_pct" in df.columns:
        score += df["net_profit_margin_pct"].fillna(0)

    if "asset_turnover" in df.columns:
        score += df["asset_turnover"].fillna(0)

    if "interest_coverage" in df.columns:
        score += df["interest_coverage"].fillna(0)

    df["composite_quality_score"] = score

    return df


def run_screener(db_path, filters):
    """
    Run the screener.
    """

    df = load_financial_data(db_path)

    df = apply_filters(df, filters)

    df = calculate_composite_score(df)

    df = df.sort_values(
        by="composite_quality_score",
        ascending=False
    )

    return df


if __name__ == "__main__":

    filters = {
        "roe_min": 15,
        "debt_to_equity_max": 1,
        "fcf_min": 0,
        "revenue_cagr_min": 10
    }

    result = run_screener(
        "nifty100.db",
        filters
    )

    print(result.head(20))