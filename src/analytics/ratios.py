"""
Financial Ratio Calculations
Sprint 2
"""

import sqlite3


def net_profit_margin(net_profit, sales):
    """
    Calculate Net Profit Margin
    """
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Calculate Operating Profit Margin
    """
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity_capital, reserves):
    """
    Calculate Return on Equity (ROE)

    Formula:
    (Net Profit / (Equity Capital + Reserves)) * 100
    """
    total_equity = equity_capital + reserves

    if total_equity == 0:
        return None

    return (net_profit / total_equity) * 100


def return_on_assets(net_profit, total_assets):
    """
    Return on Assets (ROA)

    Formula:
    Net Profit / Total Assets * 100
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


def return_on_capital_employed(
    operating_profit,
    other_income,
    equity_capital,
    reserves,
    borrowings
):
    """
    Return on Capital Employed (ROCE)

    Formula:
    EBIT / (Equity + Reserves + Borrowings) * 100
    """

    # Handle NULL values from SQLite
    if operating_profit is None:
        operating_profit = 0

    if other_income is None:
        other_income = 0

    if equity_capital is None:
        equity_capital = 0

    if reserves is None:
        reserves = 0

    if borrowings is None:
        borrowings = 0

    ebit = operating_profit + other_income

    capital_employed = (
        equity_capital +
        reserves +
        borrowings
    )

    if capital_employed <= 0:
        return None

    return (ebit / capital_employed) * 100

def interest_coverage_ratio(
    operating_profit,
    other_income,
    interest
):
    """
    Interest Coverage Ratio (ICR)

    Formula:
    (Operating Profit + Other Income) / Interest
    """

    if operating_profit is None:
        operating_profit = 0

    if other_income is None:
        other_income = 0

    if interest is None or interest == 0:
        return None

    ebit = operating_profit + other_income

    return ebit / interest
    """
    Interest Coverage Ratio (ICR)

    Formula:
    (Operating Profit + Other Income) / Interest
    """

    # Handle NULL values from SQLite
    if operating_profit is None:
        operating_profit = 0

    if other_income is None:
        other_income = 0

    if interest is None:
        interest = 0

    # Avoid division by zero
    if interest == 0:
        return None

    ebit = operating_profit + other_income

    return ebit / interest

def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Calculate Debt-to-Equity Ratio

    Formula:
    Borrowings / (Equity Capital + Reserves)
    """
    total_equity = equity_capital + reserves

    if total_equity == 0:
        return None

    return borrowings / total_equity

def asset_turnover(sales, total_assets):
    """
    Calculate Asset Turnover Ratio

    Formula:
    Sales / Total Assets
    """

    if sales is None:
        sales = 0

    if total_assets is None:
        total_assets = 0

    if total_assets == 0:
        return None

    return sales / total_assets


def calculate_all_net_profit_margins(db_path):
    """
    Calculate Net Profit Margin for all companies
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, year, sales, net_profit
        FROM profitandloss
    """)

    rows = cursor.fetchall()

    print("-" * 60)
    print("Company ID | Year | Net Profit Margin (%)")
    print("-" * 60)

    for company_id, year, sales, net_profit in rows:

        npm = net_profit_margin(net_profit, sales)

        if npm is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {npm:.2f}")

    conn.close()


def calculate_all_roe(db_path):
    """
    Calculate ROE for all companies
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.company_id,
            p.year,
            p.net_profit,
            b.equity_capital,
            b.reserves
        FROM profitandloss p
        JOIN balancesheet b
            ON p.company_id = b.company_id
            AND p.year = b.year
    """)

    rows = cursor.fetchall()

    print("-" * 75)
    print("Company ID | Year | Return on Equity (%)")
    print("-" * 75)

    for company_id, year, net_profit, equity_capital, reserves in rows:

        roe = return_on_equity(
            net_profit,
            equity_capital,
            reserves
        )

        if roe is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {roe:.2f}")

    conn.close()


def calculate_all_debt_to_equity(db_path):
    """
    Calculate Debt-to-Equity Ratio for all companies
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            company_id,
            year,
            borrowings,
            equity_capital,
            reserves
        FROM balancesheet
    """)

    rows = cursor.fetchall()

    print("-" * 75)
    print("Company ID | Year | Debt-to-Equity Ratio")
    print("-" * 75)

    for company_id, year, borrowings, equity_capital, reserves in rows:

        ratio = debt_to_equity(
            borrowings,
            equity_capital,
            reserves
        )

        if ratio is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {ratio:.2f}")

    conn.close()


def calculate_all_roce(db_path):
    """
    Calculate ROCE for all companies
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.company_id,
            p.year,
            p.operating_profit,
            p.other_income,
            b.equity_capital,
            b.reserves,
            b.borrowings
        FROM profitandloss p
        JOIN balancesheet b
            ON p.company_id = b.company_id
            AND p.year = b.year
    """)

    rows = cursor.fetchall()

    print("-" * 80)
    print("Company ID | Year | ROCE (%)")
    print("-" * 80)

    for (
        company_id,
        year,
        operating_profit,
        other_income,
        equity_capital,
        reserves,
        borrowings
    ) in rows:

        roce = return_on_capital_employed(
            operating_profit,
            other_income,
            equity_capital,
            reserves,
            borrowings
        )

        if roce is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {roce:.2f}")

def calculate_all_interest_coverage(db_path):
    """
    Calculate Interest Coverage Ratio (ICR) for all companies.
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            company_id,
            year,
            operating_profit,
            other_income,
            interest
        FROM profitandloss
    """)

    rows = cursor.fetchall()

    print("-" * 80)
    print("Company ID | Year | Interest Coverage Ratio")
    print("-" * 80)

    for (
        company_id,
        year,
        operating_profit,
        other_income,
        interest
    ) in rows:

        icr = interest_coverage_ratio(
            operating_profit,
            other_income,
            interest
        )
        if roce is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {roce:.2f}")

    conn.close()

def net_debt(borrowings, investments):
    """
    Calculate Net Debt

    Formula:
    Borrowings - Investments
    """

    if borrowings is None:
        borrowings = 0

    if investments is None:
        investments = 0

    return borrowings - investments


def calculate_all_net_debt(db_path):
    """
    Calculate Net Debt for all companies
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            company_id,
            year,
            borrowings,
            investments
        FROM balancesheet
    """)

    rows = cursor.fetchall()

    print("-" * 75)
    print("Company ID | Year | Net Debt")
    print("-" * 75)

    for company_id, year, borrowings, investments in rows:

        debt = net_debt(
            borrowings,
            investments
        )

        print(f"{company_id} | {year} | {debt}")

    conn.close()

def calculate_all_asset_turnover(db_path):
    """
    Calculate Asset Turnover for all companies
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.company_id,
            p.year,
            p.sales,
            b.total_assets
        FROM profitandloss p
        JOIN balancesheet b
            ON p.company_id = b.company_id
            AND p.year = b.year
    """)

    rows = cursor.fetchall()

    print("-" * 80)
    print("Company ID | Year | Asset Turnover")
    print("-" * 80)

    for (
        company_id,
        year,
        sales,
        total_assets
    ) in rows:

        ratio = asset_turnover(
            sales,
            total_assets
        )

        if ratio is None:
            print(f"{company_id} | {year} | None")
        else:
            print(f"{company_id} | {year} | {ratio:.2f}")

    conn.close()

def free_cash_flow(
    operating_activity,
    investing_activity
):
    """
    Calculate Free Cash Flow (FCF)

    Formula:
    Operating Activity + Investing Activity
    """

    if operating_activity is None:
        operating_activity = 0

    if investing_activity is None:
        investing_activity = 0

    return operating_activity + investing_activity

def calculate_all_free_cash_flow(db_path):
    """
    Calculate Free Cash Flow (FCF) for all companies
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            company_id,
            year,
            operating_activity,
            investing_activity
        FROM cashflow
    """)

    rows = cursor.fetchall()

    print("-" * 80)
    print("Company ID | Year | Free Cash Flow")
    print("-" * 80)

    for (
        company_id,
        year,
        operating_activity,
        investing_activity
    ) in rows:

        fcf = free_cash_flow(
            operating_activity,
            investing_activity
        )

        print(f"{company_id} | {year} | {fcf:.2f}")

    conn.close()    
   