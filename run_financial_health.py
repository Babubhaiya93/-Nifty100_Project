import sqlite3
import csv

from src.analytics.financial_health import financial_health_score
from src.analytics.ratios import (
    return_on_equity,
    return_on_capital_employed,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover
)

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    p.company_id,
    p.year,
    p.net_profit,
    p.operating_profit,
    p.other_income,
    p.interest,
    p.sales,
    b.equity_capital,
    b.reserves,
    b.borrowings,
    b.total_assets
FROM profitandloss p
JOIN balancesheet b
ON p.company_id = b.company_id
AND p.year = b.year
""")

rows = cursor.fetchall()

with open(
    "output/financial_health_scores.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "company_id",
        "year",
        "ROE",
        "ROCE",
        "Debt_Equity",
        "Interest_Coverage",
        "Asset_Turnover",
        "Health_Score"
    ])

    for row in rows:

        (
            company_id,
            year,
            net_profit,
            operating_profit,
            other_income,
            interest,
            sales,
            equity_capital,
            reserves,
            borrowings,
            total_assets
        ) = row

        roe = return_on_equity(
            net_profit,
            equity_capital,
            reserves
        )

        roce = return_on_capital_employed(
            operating_profit,
            other_income,
            equity_capital,
            reserves,
            borrowings
        )

        de = debt_to_equity(
            borrowings,
            equity_capital,
            reserves
        )

        icr = interest_coverage_ratio(
    operating_profit,
    other_income,
    interest
        )

        at = asset_turnover(
            sales,
            total_assets
        )

        score = financial_health_score(
            roe,
            roce,
            de,
            icr,
            at
        )

        writer.writerow([
            company_id,
            year,
            roe,
            roce,
            de,
            icr,
            at,
            score
        ])

conn.close()

print("financial_health_scores.csv generated successfully!")