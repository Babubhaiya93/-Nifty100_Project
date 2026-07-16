"""
Capital Allocation Screen
Sprint 4 - Day 25
"""

import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

st.title("💰 Capital Allocation Map")

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

try:
    df = pd.read_csv("output/capital_allocation.csv")

except Exception as e:
    st.error(f"Unable to load capital allocation data.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Treemap
# -------------------------------------------------------

if "capital_pattern" in df.columns:

    fig = px.treemap(
        df,
        path=["capital_pattern", "company_id"],
        values="market_cap_crore" if "market_cap_crore" in df.columns else None,
        color="capital_pattern",
        title="Capital Allocation Patterns"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------------
# Pattern Selection
# -------------------------------------------------------

patterns = sorted(df["capital_pattern"].dropna().unique())

selected = st.selectbox(
    "Select Capital Allocation Pattern",
    patterns
)

filtered = df[df["capital_pattern"] == selected]

st.subheader(f"{selected} Companies")

st.dataframe(
    filtered,
    use_container_width=True
)

st.success(f"Total Companies : {len(filtered)}")