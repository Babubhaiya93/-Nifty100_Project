from src.analytics.portfolio import generate_portfolio

result = generate_portfolio("nifty100.db")

print("=" * 60)
print("TOP 20 PORTFOLIO STOCKS")
print("=" * 60)

print(result.head(20))