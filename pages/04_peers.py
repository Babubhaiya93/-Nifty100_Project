"""
Peer Comparison Screen
Sprint 4 - Day 24
"""

import streamlit as st
import plotly.express as px

from src.dashboard.utils.db import (
    get_sectors,
    get_peers
)

st.set_page_config(layout="wide")

st.title("📊 Peer Comparison")

# --------------------------------------------------
# Load Sector Data
# --------------------------------------------------

sectors = get_sectors()

sector_list = sorted(
    sectors["broad_sector"].dropna().unique()
)

selected_sector = st.selectbox(
    "Select Sector",
    sector_list
)

# --------------------------------------------------
# Load Peer Data
# --------------------------------------------------

peer_df = get_peers(selected_sector)

if peer_df.empty:
    st.warning("No peer data available.")
    st.stop()

# --------------------------------------------------
# Average Percentiles
# --------------------------------------------------

metrics = [
    "return_on_equity_percentile",
    "net_profit_margin_percentile",
    "asset_turnover_percentile",
    "free_cash_flow_cr_percentile",
    "debt_to_equity_percentile"
]

available_metrics = [
    m for m in metrics
    if m in peer_df.columns
]

avg_df = (
    peer_df[available_metrics]
    .mean()
    .reset_index()
)

avg_df.columns = [
    "Metric",
    "Average Percentile"
]

# --------------------------------------------------
# Bar Chart
# --------------------------------------------------

fig = px.bar(
    avg_df,
    x="Metric",
    y="Average Percentile",
    title=f"{selected_sector} Average Percentiles"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# Peer Table
# --------------------------------------------------

st.subheader("Peer Companies")

st.dataframe(
    peer_df,
    use_container_width=True
)