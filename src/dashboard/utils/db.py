"""
Database Utility Functions
Sprint 4 - Day 22
"""

import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "nifty100.db"


@st.cache_data(ttl=600)
def get_companies():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT * FROM companies ORDER BY company_id",
        conn
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_ratios(ticker, year=None):

    conn = sqlite3.connect(DB_PATH)

    if year is None:
        query = """
        SELECT *
        FROM financial_ratios
        WHERE company_id = ?
        ORDER BY year
        """
        df = pd.read_sql_query(
            query,
            conn,
            params=(ticker,)
        )

    else:
        query = """
        SELECT *
        FROM financial_ratios
        WHERE company_id = ?
        AND year = ?
        """
        df = pd.read_sql_query(
            query,
            conn,
            params=(ticker, year)
        )

    conn.close()
    return df


@st.cache_data(ttl=600)
def get_pl(ticker):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM profitandloss
        WHERE company_id=?
        ORDER BY year
        """,
        conn,
        params=(ticker,)
    )

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_bs(ticker):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM balancesheet
        WHERE company_id=?
        ORDER BY year
        """,
        conn,
        params=(ticker,)
    )

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_cf(ticker):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM cashflow
        WHERE company_id=?
        ORDER BY year
        """,
        conn,
        params=(ticker,)
    )

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_sectors():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM sectors",
        conn
    )

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_peers(group_name):

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT *
    FROM peer_percentiles
    WHERE broad_sector=?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(group_name,)
    )

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_valuation(ticker):

    conn = sqlite3.connect(DB_PATH)

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM valuation_summary
            WHERE company_id=?
            """,
            conn,
            params=(ticker,)
        )

    except Exception:

        df = pd.DataFrame()

    conn.close()

    return df