from src.analytics.cashflow_kpis import capital_allocation_pattern

print("Test 1:", capital_allocation_pattern(100, -50, -20))
print("Test 2:", capital_allocation_pattern(-100, 50, 20))
print("Test 3:", capital_allocation_pattern(-50, -100, 200))
print("Test 4:", capital_allocation_pattern(100, 50, 60))
print("Test 5:", capital_allocation_pattern(-100, -50, -60))
print("Test 6:", capital_allocation_pattern(100, -20, 80))