"""
Company Comparison Engine
Sprint 3 - Day 20
"""

import sqlite3
import pandas as pd


def load_company_data(db_path):

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


def compare_companies(df, companies):

    df = df[
        df["company_id"].isin(companies)
    ]

    columns = [
        "company_id",
        "year",
        "broad_sector",
        "return_on_equity_pct",
        "net_profit_margin_pct",
        "interest_coverage",
        "asset_turnover",
        "free_cash_flow_cr",
        "debt_to_equity"
    ]

    available_columns = [
        col for col in columns
        if col in df.columns
    ]

    return df[available_columns]


def export_comparison(df):

    output_file = "output/company_comparison.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("COMPANY COMPARISON GENERATED")
    print("=" * 60)
    print("Output :", output_file)
    print("Rows   :", len(df))


def run_company_comparison(db_path, companies):

    df = load_company_data(db_path)

    comparison = compare_companies(df, companies)

    export_comparison(comparison)

    return comparison


if __name__ == "__main__":

    companies = [
        "ABB",
        "BEL",
        "HAL",
        "INFY"
    ]

    result = run_company_comparison(
        "nifty100.db",
        companies
    )

    print(result.head(20))