from src.analytics.ratios import return_on_equity

print("Test 1:", return_on_equity(100, 500, 500))
print("Test 2:", return_on_equity(200, 1000, 500))
print("Test 3:", return_on_equity(100, 0, 0))