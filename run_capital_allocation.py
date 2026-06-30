import sqlite3
import csv

from src.analytics.cashflow_kpis import capital_allocation_pattern

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    company_id,
    year,
    operating_activity,
    investing_activity,
    financing_activity
FROM cashflow
""")

rows = cursor.fetchall()

with open(
    "output/capital_allocation.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "company_id",
        "year",
        "cfo_sign",
        "cfi_sign",
        "cff_sign",
        "pattern_label"
    ])

    for (
        company_id,
        year,
        operating_activity,
        investing_activity,
        financing_activity
    ) in rows:

        # Handle NULL values
        if operating_activity is None:
            operating_activity = 0

        if investing_activity is None:
            investing_activity = 0

        if financing_activity is None:
            financing_activity = 0

        cfo_sign = "+" if operating_activity >= 0 else "-"
        cfi_sign = "+" if investing_activity >= 0 else "-"
        cff_sign = "+" if financing_activity >= 0 else "-"

        pattern = capital_allocation_pattern(
            operating_activity,
            investing_activity,
            financing_activity
        )

        writer.writerow([
            company_id,
            year,
            cfo_sign,
            cfi_sign,
            cff_sign,
            pattern
        ])

conn.close()

print("capital_allocation.csv generated successfully!")