"""
Trend Analysis Screen
Sprint 4 - Day 25
"""

import streamlit as st
import plotly.express as px

from src.dashboard.utils.db import (
    get_companies,
    get_pl
)

st.set_page_config(layout="wide")

st.title("📈 Trend Analysis")

# ---------------------------------------
# Company Selection
# ---------------------------------------

companies = get_companies()

ticker = st.selectbox(
    "Select Company",
    companies["company_id"].sort_values().unique()
)

# ---------------------------------------
# Load Data
# ---------------------------------------

df = get_pl(ticker)

if df.empty:
    st.warning("No financial data available.")
    st.stop()

# ---------------------------------------
# Metric Selection
# ---------------------------------------

available_metrics = []

possible_metrics = [
    "sales",
    "net_profit",
    "operating_profit",
    "expenses"
]

for metric in possible_metrics:
    if metric in df.columns:
        available_metrics.append(metric)

selected_metric = st.selectbox(
    "Select Financial Metric",
    available_metrics
)

# ---------------------------------------
# Trend Chart
# ---------------------------------------

fig = px.line(
    df,
    x="year",
    y=selected_metric,
    markers=True,
    title=f"{ticker} - {selected_metric.replace('_',' ').title()} Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# Financial Data Table
# ---------------------------------------

st.subheader("Financial Data")

st.dataframe(
    df,
    use_container_width=True
)