from src.analytics.ratios import debt_to_equity

print("Test 1:", debt_to_equity(500, 500, 500))
print("Test 2:", debt_to_equity(200, 1000, 500))
print("Test 3:", debt_to_equity(100, 0, 0))