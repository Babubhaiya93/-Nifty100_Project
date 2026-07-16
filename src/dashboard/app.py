"""
Nifty 100 Financial Analytics Dashboard
Sprint 4 - Day 22
Main Streamlit Application
"""

import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Nifty 100 Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Screen",
    [
        "Home",
        "Company Profile",
        "Stock Screener",
        "Peer Comparison",
        "Trend Analysis",
        "Sector Analysis",
        "Capital Allocation",
        "Annual Reports"
    ]
)

# --------------------------------------------------
# Main Area
# --------------------------------------------------

st.title("📈 Nifty 100 Financial Analytics Dashboard")

st.markdown("---")

if page == "Home":
    st.header("🏠 Home")
    st.info("Home Screen - Coming in Day 23")

elif page == "Company Profile":
    st.header("🏢 Company Profile")
    st.info("Company Profile Screen - Coming in Day 23")

elif page == "Stock Screener":
    st.header("🔍 Stock Screener")
    st.info("Stock Screener Screen - Coming in Day 24")

elif page == "Peer Comparison":
    st.header("📊 Peer Comparison")
    st.info("Peer Comparison Screen - Coming in Day 24")

elif page == "Trend Analysis":
    st.header("📈 Trend Analysis")
    st.info("Trend Analysis Screen - Coming in Day 25")

elif page == "Sector Analysis":
    st.header("🏭 Sector Analysis")
    st.info("Sector Analysis Screen - Coming in Day 25")

elif page == "Capital Allocation":
    st.header("💰 Capital Allocation")
    st.info("Capital Allocation Screen - Coming in Day 25")

elif page == "Annual Reports":
    st.header("📄 Annual Reports")
    st.info("Annual Reports Screen - Coming in Day 25")