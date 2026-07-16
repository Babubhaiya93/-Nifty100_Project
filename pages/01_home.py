"""
Home Dashboard
Sprint 4 - Day 23
"""

import streamlit as st
import plotly.express as px

from src.dashboard.utils.db import (
    get_companies,
    get_ratios,
    get_sectors
)

st.set_page_config(layout="wide")

st.title("🏠 Nifty 100 Analytics Dashboard")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

companies = get_companies()
ratios = get_ratios("ABB")
sectors = get_sectors()

# ---------------------------------------------------
# KPI Tiles
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Companies",
        len(companies)
    )

with col2:
    if "return_on_equity_pct" in ratios.columns:
        st.metric(
            "Average ROE",
            round(
                ratios["return_on_equity_pct"].mean(),
                2
            )
        )

with col3:
    st.metric(
        "Total Sectors",
        sectors["broad_sector"].nunique()
    )

st.divider()

# ---------------------------------------------------
# Sector Distribution
# ---------------------------------------------------

sector_count = (
    sectors.groupby("broad_sector")
    .size()
    .reset_index(name="Companies")
)

fig = px.pie(
    sector_count,
    values="Companies",
    names="broad_sector",
    title="Sector Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Company List
# ---------------------------------------------------

st.subheader("Companies")

st.dataframe(
    companies,
    use_container_width=True
)