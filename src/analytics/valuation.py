"""
Sprint 4 - Day 26
Valuation Module
"""

import sqlite3
import pandas as pd


def generate_valuation(db_path="nifty100.db"):

    # -------------------------------
    # Load Financial Ratios
    # -------------------------------

    conn = sqlite3.connect(db_path)

    ratios = pd.read_sql("""
        SELECT
            company_id,
            year,
            free_cash_flow_cr
        FROM financial_ratios
    """, conn)

    sectors = pd.read_sql("""
        SELECT
            company_id,
            broad_sector
        FROM sectors
    """, conn)

    conn.close()

    # -------------------------------
    # Load Market Cap Excel
    # -------------------------------

    valuation = pd.read_excel(
        "data/raw/market_cap.xlsx"
    )

    valuation["year"] = valuation["year"].astype(str)
    ratios["year"] = ratios["year"].astype(str)

    # -------------------------------
    # Merge Data
    # -------------------------------

    df = pd.merge(
        valuation,
        ratios,
        on=["company_id", "year"],
        how="left"
    )

    df = pd.merge(
        df,
        sectors,
        on="company_id",
        how="left"
    )

    # -------------------------------
    # FCF Yield
    # -------------------------------

    df["fcf_yield_pct"] = (
        df["free_cash_flow_cr"] /
        df["market_cap_crore"]
    ) * 100

    # -------------------------------
    # Sector Median PE
    # -------------------------------

    sector_pe = (
        df.groupby("broad_sector")["pe_ratio"]
        .median()
        .reset_index()
    )

    sector_pe.rename(
        columns={
            "pe_ratio": "sector_median_pe"
        },
        inplace=True
    )

    df = pd.merge(
        df,
        sector_pe,
        on="broad_sector",
        how="left"
    )

    df["pe_vs_sector_pct"] = (
        df["pe_ratio"] /
        df["sector_median_pe"]
    ) * 100

    # -------------------------------
    # Valuation Flag
    # -------------------------------

    def valuation_flag(row):

        if pd.isna(row["pe_ratio"]) or pd.isna(row["sector_median_pe"]):
            return "N/A"

        if row["pe_ratio"] > row["sector_median_pe"] * 1.5:
            return "Caution"

        elif row["pe_ratio"] < row["sector_median_pe"] * 0.7:
            return "Discount"

        else:
            return "Fair"

    df["flag"] = df.apply(valuation_flag, axis=1)

    # -------------------------------
    # Select Output Columns
    # -------------------------------

    summary = df[
        [
            "company_id",
            "year",
            "broad_sector",
            "market_cap_crore",
            "enterprise_value_crore",
            "pe_ratio",
            "pb_ratio",
            "ev_ebitda",
            "dividend_yield_pct",
            "free_cash_flow_cr",
            "fcf_yield_pct",
            "sector_median_pe",
            "pe_vs_sector_pct",
            "flag",
        ]
    ]

    # -------------------------------
    # Save Files
    # -------------------------------

    summary.to_excel(
        "output/valuation_summary.xlsx",
        index=False
    )

    summary[
        summary["flag"].isin(["Caution", "Discount"])
    ].to_csv(
        "output/valuation_flags.csv",
        index=False
    )

    print("=" * 60)
    print("VALUATION MODULE COMPLETED")
    print("=" * 60)
    print("Companies :", len(summary))
    print("Excel :", "output/valuation_summary.xlsx")
    print("CSV   :", "output/valuation_flags.csv")
    print("=" * 60)

    print(summary.head(20))


if __name__ == "__main__":
    generate_valuation()