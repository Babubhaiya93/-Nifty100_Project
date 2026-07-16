"""
Sector Analysis Screen
Sprint 4 - Day 25
"""

import streamlit as st
import plotly.express as px

from src.dashboard.utils.db import (
    get_sectors,
    get_ratios
)

st.set_page_config(layout="wide")

st.title("🏭 Sector Analysis")

# ----------------------------------------------------
# Load Sector List
# ----------------------------------------------------

sector_df = get_sectors()

sector_list = sorted(
    sector_df["broad_sector"].dropna().unique()
)

selected_sector = st.selectbox(
    "Select Sector",
    sector_list
)

# ----------------------------------------------------
# Load Financial Ratios
# ----------------------------------------------------

df = get_ratios("ABB")

if df.empty:
    st.warning("No financial ratio data found.")
    st.stop()

# ----------------------------------------------------
# Merge Sector Information
# ----------------------------------------------------

df = df.merge(
    sector_df,
    on="company_id",
    how="left"
)

sector_data = df[
    df["broad_sector"] == selected_sector
]

if sector_data.empty:
    st.warning("No companies found.")
    st.stop()

# ----------------------------------------------------
# Bubble Chart
# ----------------------------------------------------

if (
    "sales" in sector_data.columns and
    "return_on_equity_pct" in sector_data.columns
):

    fig = px.scatter(
        sector_data,
        x="sales",
        y="return_on_equity_pct",
        size="sales",
        color="company_id",
        hover_name="company_id",
        title=f"{selected_sector} Companies"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# Sector KPI Summary
# ----------------------------------------------------

st.subheader("Sector Statistics")

summary = sector_data.describe()

st.dataframe(
    summary,
    use_container_width=True
)

# ----------------------------------------------------
# Company List
# ----------------------------------------------------

st.subheader("Companies")

st.dataframe(
    sector_data,
    use_container_width=True
)