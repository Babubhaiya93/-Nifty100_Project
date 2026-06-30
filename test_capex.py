from src.analytics.cashflow_kpis import capex_intensity

print("Test 1:", capex_intensity(-20, 1000))
print("Test 2:", capex_intensity(-50, 1000))
print("Test 3:", capex_intensity(-120, 1000))
print("Test 4:", capex_intensity(-100, 0))