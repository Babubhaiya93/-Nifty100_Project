"""
Company Profile Screen
Sprint 4 - Day 23
"""

import streamlit as st
import plotly.express as px

from src.dashboard.utils.db import (
    get_companies,
    get_ratios,
    get_pl,
    get_sectors
)

st.set_page_config(layout="wide")

st.title("🏢 Company Profile")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

companies = get_companies()

ticker = st.selectbox(
    "Select Company",
    companies["company_id"].sort_values().unique()
)

ratios = get_ratios(ticker)
pl = get_pl(ticker)
sector = get_sectors()

# --------------------------------------------------
# Company Information
# --------------------------------------------------

st.subheader("Company Information")

company_sector = sector[
    sector["company_id"] == ticker
]

if not company_sector.empty:

    st.write("**Company:**", ticker)

    st.write(
        "**Sector:**",
        company_sector.iloc[0]["broad_sector"]
    )

# --------------------------------------------------
# KPI Tiles
# --------------------------------------------------

if not ratios.empty:

    latest = ratios.iloc[-1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ROE",
            round(
                latest.get("return_on_equity_pct", 0),
                2
            )
        )

    with col2:
        st.metric(
            "Net Profit Margin",
            round(
                latest.get("net_profit_margin_pct", 0),
                2
            )
        )

    with col3:
        st.metric(
            "Debt to Equity",
            round(
                latest.get("debt_to_equity", 0),
                2
            )

        )

st.divider()

# --------------------------------------------------
# Revenue Chart
# --------------------------------------------------

if not pl.empty and "sales" in pl.columns:

    fig = px.bar(
        pl,
        x="year",
        y="sales",
        title="Revenue Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# Profit Chart
# --------------------------------------------------

if not pl.empty and "net_profit" in pl.columns:

    fig2 = px.line(
        pl,
        x="year",
        y="net_profit",
        markers=True,
        title="Net Profit Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# --------------------------------------------------
# Financial Ratios
# --------------------------------------------------

st.subheader("Financial Ratios")

st.dataframe(
    ratios,
    use_container_width=True
)