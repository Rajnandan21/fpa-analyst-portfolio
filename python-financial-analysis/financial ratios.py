"""
financial_ratios.py
Calculates liquidity, profitability, leverage, and efficiency ratios
from a standard financial statement dataset.
"""
import pandas as pd


def calculate_ratios(df: pd.DataFrame) -> pd.DataFrame:
    ratios = pd.DataFrame()
    ratios['Year'] = df['Year']

    # ---- Profitability Ratios ----
    gross_profit = df['Revenue'] + df['COGS']
    ebit = gross_profit + df['SG&A'] - (-df['Depreciation'])  # depreciation already negative
    ratios['Gross_Margin_%'] = (gross_profit / df['Revenue'] * 100).round(1)
    ratios['Net_Margin_%'] = (df['Net_Income'] / df['Revenue'] * 100).round(1)
    ratios['ROA_%'] = (df['Net_Income'] / df['Total_Assets'] * 100).round(1)
    ratios['ROE_%'] = (df['Net_Income'] / df['Total_Equity'] * 100).round(1)

    # ---- Liquidity Ratios ----
    ratios['Current_Ratio'] = (df['Total_Current_Assets'] / df['Total_Current_Liabilities']).round(2)
    quick_assets = df['Total_Current_Assets'] - df['Inventory']
    ratios['Quick_Ratio'] = (quick_assets / df['Total_Current_Liabilities']).round(2)

    # ---- Leverage Ratios ----
    ratios['Debt_to_Equity'] = (df['Total_Liabilities'] / df['Total_Equity']).round(2)
    ebit_calc = df['Revenue'] + df['COGS'] + df['SG&A'] + df['Depreciation']
    ratios['Interest_Coverage'] = (ebit_calc / -df['Interest_Expense']).round(2)

    # ---- Efficiency Ratios ----
    ratios['Asset_Turnover'] = (df['Revenue'] / df['Total_Assets']).round(2)
    ratios['Inventory_Turnover'] = (-df['COGS'] / df['Inventory']).round(2)
    ratios['Receivables_Turnover'] = (df['Revenue'] / df['Accounts_Receivable']).round(2)
    ratios['DSO_days'] = (365 / ratios['Receivables_Turnover']).round(0)
    ratios['DIO_days'] = (365 / ratios['Inventory_Turnover']).round(0)
    dpo_denom = -df['COGS']
    ratios['DPO_days'] = (df['Accounts_Payable'] / dpo_denom * 365).round(0)
    ratios['Cash_Conversion_Cycle_days'] = (
        ratios['DSO_days'] + ratios['DIO_days'] - ratios['DPO_days']
    ).round(0)

    return ratios


if __name__ == '__main__':
    df = pd.read_csv('/home/claude/python_project/financial_statements.csv')
    ratios = calculate_ratios(df)
    ratios.to_csv('/home/claude/python_project/financial_ratios_output.csv', index=False)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 20)
    print(ratios.T)
