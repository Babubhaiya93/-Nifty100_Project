"""
Cash Flow KPI Calculations
Sprint 2
"""


def cfo_quality_score(cfo, pat):
    """
    CFO / PAT Quality Score

    >1.0  -> High Quality
    0.5-1 -> Moderate
    <0.5  -> Accrual Risk
    """

    if cfo is None:
        cfo = 0

    if pat is None:
        pat = 0

    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1.0:
        return "High Quality"
    elif ratio >= 0.5:
        return "Moderate"
    else:
        return "Accrual Risk"

def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity

    Formula:
    abs(Investing Activity) / Sales * 100

    <3%  -> Asset Light
    3-8% -> Moderate
    >8%  -> Capital Intensive
    """

    if investing_activity is None:
        investing_activity = 0

    if sales is None:
        sales = 0

    if sales == 0:
        return None

    ratio = (abs(investing_activity) / sales) * 100

    if ratio < 3:
        return "Asset Light"

    elif ratio <= 8:
        return "Moderate"

    else:
        return "Capital Intensive"

def fcf_conversion_rate(free_cash_flow, operating_profit):
    """
    Free Cash Flow Conversion Rate

    Formula:
    FCF / Operating Profit * 100
    """

    if free_cash_flow is None:
        free_cash_flow = 0

    if operating_profit is None:
        operating_profit = 0

    if operating_profit == 0:
        return None

    return (free_cash_flow / operating_profit) * 100
def capital_allocation_pattern(
    operating_activity,
    investing_activity,
    financing_activity
):
    """
    Classify capital allocation pattern
    """

    if operating_activity is None:
        operating_activity = 0

    if investing_activity is None:
        investing_activity = 0

    if financing_activity is None:
        financing_activity = 0

    cfo = "+" if operating_activity >= 0 else "-"
    cfi = "+" if investing_activity >= 0 else "-"
    cff = "+" if financing_activity >= 0 else "-"

    pattern = (cfo, cfi, cff)

    if pattern == ("+", "-", "-"):
        return "Reinvestor"
    elif pattern == ("+", "+", "-"):
        return "Liquidating Assets"
    elif pattern == ("-", "+", "+"):
        return "Distress Signal"
    elif pattern == ("-", "-", "+"):
        return "Growth Funded by Debt"
    elif pattern == ("+", "+", "+"):
        return "Cash Accumulator"
    elif pattern == ("-", "-", "-"):
        return "Pre-Revenue"
    elif pattern == ("+", "-", "+"):
        return "Mixed"
    else:
        return "Other"