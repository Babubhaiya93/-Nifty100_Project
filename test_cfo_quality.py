from src.analytics.cashflow_kpis import cfo_quality_score

print("Test 1:", cfo_quality_score(1200, 1000))
print("Test 2:", cfo_quality_score(700, 1000))
print("Test 3:", cfo_quality_score(300, 1000))
print("Test 4:", cfo_quality_score(1000, 0))