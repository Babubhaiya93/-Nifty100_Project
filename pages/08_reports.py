"""
Annual Reports Screen
Sprint 4 - Day 25
"""

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📄 Annual Reports")

# -------------------------------------------------------
# Load Reports
# -------------------------------------------------------

try:
    df = pd.read_csv("output/company_comparison.csv")

except Exception as e:
    st.error(f"Unable to load report data.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Company Selection
# -------------------------------------------------------

companies = sorted(df["company_id"].unique())

company = st.selectbox(
    "Select Company",
    companies
)

company_df = df[df["company_id"] == company]

st.subheader(f"Annual Reports - {company}")

# -------------------------------------------------------
# Show Available Years
# -------------------------------------------------------

years = sorted(company_df["year"].unique())

for year in years:

    st.markdown(f"### {year}")

    st.write("📄 Annual Report Available")

    st.link_button(
        "Open BSE Annual Report",
        "https://www.bseindia.com/"
    )

st.success(f"Available Reports : {len(years)}")