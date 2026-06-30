from src.analytics.ratios import return_on_capital_employed

print(
    "Test 1:",
    return_on_capital_employed(
        500,
        50,
        1000,
        3000,
        1000
    )
)

print(
    "Test 2:",
    return_on_capital_employed(
        100,
        20,
        500,
        500,
        0
    )
)

print(
    "Test 3:",
    return_on_capital_employed(
        100,
        20,
        0,
        0,
        0
    )
)