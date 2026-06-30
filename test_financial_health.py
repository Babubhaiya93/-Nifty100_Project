from src.analytics.financial_health import financial_health_score

print("Test 1:", financial_health_score(25, 22, 0.3, 8, 2.5))
print("Test 2:", financial_health_score(16, 17, 0.8, 4, 1.2))
print("Test 3:", financial_health_score(12, 11, 1.8, 2, 0.6))
print("Test 4:", financial_health_score(5, 8, 3, 1, 0.3))