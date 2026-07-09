"""
Peer Percentile Ranking Engine
Sprint 3 - Day 18
"""

import sqlite3
import pandas as pd


def load_peer_data(db_path):
    """
    Load financial ratios with sector information.
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


def calculate_percentiles(df):

    metrics = [
        "return_on_equity_pct",
        "net_profit_margin_pct",
        "interest_coverage",
        "asset_turnover",
        "free_cash_flow_cr"
    ]

    # Higher value = better
    for metric in metrics:

        if metric in df.columns:

            df[metric + "_percentile"] = (
                df.groupby("broad_sector")[metric]
                .rank(pct=True) * 100
            )

    # Lower Debt-to-Equity = Better
    if "debt_to_equity" in df.columns:

        df["debt_to_equity_percentile"] = (
            100 -
            (
                df.groupby("broad_sector")["debt_to_equity"]
                .rank(pct=True) * 100
            )
        )

    return df


def export_peer_percentiles(df):

    output_file = "output/peer_percentiles.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("PEER PERCENTILES GENERATED")
    print("=" * 60)
    print("Output :", output_file)
    print("Rows   :", len(df))


def save_to_sqlite(df, db_path):
    """
    Save percentile data into SQLite table.
    """

    conn = sqlite3.connect(db_path)

    columns = [
        "company_id",
        "year",
        "broad_sector",
        "return_on_equity_pct_percentile",
        "net_profit_margin_pct_percentile",
        "interest_coverage_percentile",
        "asset_turnover_percentile",
        "free_cash_flow_cr_percentile",
        "debt_to_equity_percentile"
    ]

    # Keep only columns that actually exist
    available_columns = []

    for col in columns:
        if col in df.columns:
            available_columns.append(col)

    df[available_columns].to_sql(
        "peer_percentiles",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("=" * 60)
    print("SQLite Table Updated")
    print("=" * 60)


def run_peer_engine(db_path):

    df = load_peer_data(db_path)

    df = calculate_percentiles(df)

    export_peer_percentiles(df)

    save_to_sqlite(df, db_path)

    return df


if __name__ == "__main__":

    result = run_peer_engine("nifty100.db")

    print(result.head(20))