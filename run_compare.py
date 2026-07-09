from src.analytics.compare import run_company_comparison


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

print("=" * 60)
print("COMPANY COMPARISON")
print("=" * 60)

print(result.head(20))