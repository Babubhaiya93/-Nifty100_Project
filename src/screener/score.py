import pandas as pd


def normalize(series):
    """
    Normalize values to a 0-100 scale.
    """
    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series([50] * len(series), index=series.index)

    return ((series - minimum) / (maximum - minimum)) * 100


def calculate_composite_score(df):

    score = pd.Series(0, index=df.index)

    metrics = [
        "return_on_equity_pct",
        "net_profit_margin_pct",
        "asset_turnover",
        "interest_coverage"
    ]

    for metric in metrics:

        if metric in df.columns:
            score += normalize(df[metric].fillna(0))

    df["composite_quality_score"] = score

    return df