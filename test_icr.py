from src.analytics.ratios import interest_coverage_ratio

print("Test 1:", interest_coverage_ratio(100, 10, 10))
print("Test 2:", interest_coverage_ratio(50, 10, 5))
print("Test 3:", interest_coverage_ratio(100, 20, 0))