from src.analytics.ratios import net_debt

print("Test 1:", net_debt(500, 100))
print("Test 2:", net_debt(200, 50))
print("Test 3:", net_debt(None, 100))
print("Test 4:", net_debt(500, None))