"""
Sprint 3 - Day 19
Radar Chart Generator
"""

import sqlite3
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        fr.company_id,
        fr.year,
        fr.return_on_equity_pct,
        fr.net_profit_margin_pct,
        fr.asset_turnover,
        fr.interest_coverage,
        fr.free_cash_flow_cr,
        s.broad_sector
    FROM financial_ratios fr
    LEFT JOIN sectors s
    ON fr.company_id=s.company_id
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def create_radar(company_df, sector_df, company):

    metrics = [
        "return_on_equity_pct",
        "net_profit_margin_pct",
        "asset_turnover",
        "interest_coverage",
        "free_cash_flow_cr"
    ]

    company_values = company_df[metrics].fillna(0).mean().values

    sector_values = sector_df[metrics].fillna(0).mean().values

    labels = [
        "ROE",
        "NPM",
        "Asset",
        "ICR",
        "FCF"
    ]

    angles = np.linspace(
        0,
        2*np.pi,
        len(labels),
        endpoint=False
    )

    company_values = np.concatenate(
        (company_values,[company_values[0]])
    )

    sector_values = np.concatenate(
        (sector_values,[sector_values[0]])
    )

    angles = np.concatenate(
        (angles,[angles[0]])
    )

    plt.figure(figsize=(6,6))

    ax = plt.subplot(111, polar=True)

    ax.plot(angles, company_values)

    ax.fill(angles, company_values, alpha=0.25)

    ax.plot(
        angles,
        sector_values,
        linestyle="--"
    )

    ax.set_xticks(angles[:-1])

    ax.set_xticklabels(labels)

    plt.title(company)

    output = f"reports/radar_charts/{company}_radar.png"

    plt.savefig(output)

    plt.close()


def generate_all(db_path):

    df = load_data(db_path)

    os.makedirs(
        "reports/radar_charts",
        exist_ok=True
    )

    companies = df["company_id"].unique()

    count = 0

    for company in companies:

        company_df = df[
            df["company_id"]==company
        ]

        sector = company_df[
            "broad_sector"
        ].iloc[0]

        sector_df = df[
            df["broad_sector"]==sector
        ]

        create_radar(
            company_df,
            sector_df,
            company
        )

        count += 1

    print("="*60)
    print("RADAR CHARTS GENERATED")
    print("="*60)
    print("Charts :", count)
    print("Folder : reports/radar_charts")


if __name__=="__main__":

    generate_all("nifty100.db")