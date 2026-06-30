from src.analytics.ratios import free_cash_flow

print("Test 1:", free_cash_flow(1000, -300))
print("Test 2:", free_cash_flow(800, -1200))
print("Test 3:", free_cash_flow(None, -100))
print("Test 4:", free_cash_flow(500, None))