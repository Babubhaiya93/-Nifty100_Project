from src.screener.engine import run_screener

from src.screener.presets import (
    QUALITY_COMPOUNDER,
    VALUE_PICK,
    GROWTH_ACCELERATOR,
    DIVIDEND_CHAMPION,
    DEBT_FREE_BLUECHIP,
    TURNAROUND_WATCH
)

PRESETS = {
    "Quality Compounder": QUALITY_COMPOUNDER,
    "Value Pick": VALUE_PICK,
    "Growth Accelerator": GROWTH_ACCELERATOR,
    "Dividend Champion": DIVIDEND_CHAMPION,
    "Debt Free Bluechip": DEBT_FREE_BLUECHIP,
    "Turnaround Watch": TURNAROUND_WATCH
}

for name, filters in PRESETS.items():

    print("=" * 60)
    print(name)
    print("=" * 60)

    result = run_screener(
        "nifty100.db",
        filters
    )

    print("Companies Selected :", len(result))

    filename = (
        "output/" +
        name.lower().replace(" ", "_") +
        ".csv"
    )

    result.to_csv(filename, index=False)

    print("Saved :", filename)

    print(result.head(5))

print("\nDay 16 Completed Successfully!")