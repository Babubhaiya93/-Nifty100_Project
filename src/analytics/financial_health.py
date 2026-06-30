"""
Financial Health Scoring
Sprint 2
"""


def financial_health_score(
    roe,
    roce,
    debt_equity,
    interest_coverage,
    asset_turnover
):
    """
    Returns score out of 100.
    """

    score = 0

    # ROE
    if roe is not None:
        if roe >= 20:
            score += 20
        elif roe >= 15:
            score += 15
        elif roe >= 10:
            score += 10

    # ROCE
    if roce is not None:
        if roce >= 20:
            score += 20
        elif roce >= 15:
            score += 15
        elif roce >= 10:
            score += 10

    # Debt to Equity
    if debt_equity is not None:
        if debt_equity < 0.5:
            score += 20
        elif debt_equity < 1:
            score += 15
        elif debt_equity < 2:
            score += 10

    # Interest Coverage
    if interest_coverage is not None:
        if interest_coverage >= 5:
            score += 20
        elif interest_coverage >= 3:
            score += 15
        elif interest_coverage >= 1.5:
            score += 10

    # Asset Turnover
    if asset_turnover is not None:
        if asset_turnover >= 2:
            score += 20
        elif asset_turnover >= 1:
            score += 15
        elif asset_turnover >= 0.5:
            score += 10

    return score