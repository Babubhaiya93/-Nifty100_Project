from src.screener.engine import run_screener
import pandas as pd

filters = {
    "roe_min": 15,
    "debt_to_equity_max": 1,
    "fcf_min": 0,
    "revenue_cagr_min": 10
}

df = run_screener("nifty100.db", filters)

output_file = "output/screener_output.xlsx"

df.to_excel(output_file, index=False)

print("=" * 60)
print("SCREENER EXCEL GENERATED")
print("=" * 60)
print(output_file)
print("Rows:", len(df))