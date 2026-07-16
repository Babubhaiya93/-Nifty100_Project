"""
Sprint 4 - Day 27
Integration QA & Bug Fix
"""

import os
import sqlite3
import pandas as pd

print("=" * 60)
print("SPRINT 4 - DAY 27 QA CHECK")
print("=" * 60)

# -----------------------------------
# Check Database
# -----------------------------------

try:
    conn = sqlite3.connect("nifty100.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM companies")
    companies = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM financial_ratios")
    ratios = cursor.fetchone()[0]

    conn.close()

    print("✓ Database Connected")
    print("✓ Companies :", companies)
    print("✓ Financial Ratios :", ratios)

except Exception as e:
    print("✗ Database Error")
    print(e)

print("-" * 60)

# -----------------------------------
# Check Output Files
# -----------------------------------

files = [
    "output/screener_output.csv",
    "output/company_comparison.csv",
    "output/company_ranking.csv",
    "output/portfolio_recommendation.csv",
    "output/valuation_summary.xlsx",
    "output/valuation_flags.csv"
]

for file in files:

    if os.path.exists(file):
        print("✓", file)
    else:
        print("✗ Missing:", file)

print("-" * 60)

# -----------------------------------
# Check Valuation Summary
# -----------------------------------

try:

    df = pd.read_excel("output/valuation_summary.xlsx")

    print("Rows :", len(df))
    print("Columns :", len(df.columns))

    print("\nMissing Values")

    print(df.isnull().sum())

except Exception as e:

    print("Unable to read valuation_summary.xlsx")
    print(e)

print("-" * 60)

print("QA CHECK COMPLETED")

print("=" * 60)