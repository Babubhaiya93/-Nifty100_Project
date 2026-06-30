from src.analytics.cashflow_kpis import fcf_conversion_rate

print("Test 1:", fcf_conversion_rate(700, 1000))
print("Test 2:", fcf_conversion_rate(500, 500))
print("Test 3:", fcf_conversion_rate(-200, 1000))
print("Test 4:", fcf_conversion_rate(100, 0))