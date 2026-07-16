"""
Stock Screener
Sprint 4 - Day 24
"""

import streamlit as st
import pandas as pd

from src.dashboard.utils.db import get_ratios

st.set_page_config(layout="wide")

st.title("🔍 Stock Screener")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = get_ratios("ABB")

if df.empty:
    st.error("No financial ratio data found.")
    st.stop()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("Screening Filters")

roe_min = st.sidebar.slider(
    "Minimum ROE (%)",
    0.0,
    100.0,
    10.0
)

npm_min = st.sidebar.slider(
    "Minimum Net Profit Margin (%)",
    0.0,
    100.0,
    10.0
)

de_max = st.sidebar.slider(
    "Maximum Debt to Equity",
    0.0,
    5.0,
    1.0
)

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered = df.copy()

if "return_on_equity_pct" in filtered.columns:
    filtered = filtered[
        filtered["return_on_equity_pct"] >= roe_min
    ]

if "net_profit_margin_pct" in filtered.columns:
    filtered = filtered[
        filtered["net_profit_margin_pct"] >= npm_min
    ]

if "debt_to_equity" in filtered.columns:
    filtered = filtered[
        filtered["debt_to_equity"] <= de_max
    ]

# --------------------------------------------------
# Results
# --------------------------------------------------

st.subheader("Matching Companies")

st.success(f"{len(filtered)} records found")

st.dataframe(
    filtered,
    use_container_width=True
)

# --------------------------------------------------
# Download CSV
# --------------------------------------------------

csv = filtered.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="screener_results.csv",
    mime="text/csv"
)