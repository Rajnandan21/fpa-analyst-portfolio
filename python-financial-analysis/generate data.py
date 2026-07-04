import pandas as pd

years = ['FY2022A', 'FY2023A', 'FY2024A', 'FY2025A', 'FY2026E']

data = {
    'Year': years,
    # Income Statement (£ thousands)
    'Revenue': [9800, 10650, 11800, 12850, 13750],
    'COGS': [-6370, -6817, -7434, -7957, -8388],
    'SG&A': [-1666, -1704, -2006, -2056, -2131],
    'Depreciation': [-450, -480, -510, -540, -570],
    'Interest_Expense': [-195, -180, -172, -156, -140],
    'Tax_Expense': [-325, -378, -420, -466, -505],
    'Net_Income': [794, 1091, 1258, 1675, 2016],
    # Balance Sheet (£ thousands)
    'Cash': [1200, 1350, 1650, 1820, 2100],
    'Accounts_Receivable': [1120, 1215, 1358, 1410, 1479],
    'Inventory': [980, 1050, 1120, 1180, 1210],
    'Total_Current_Assets': [3300, 3615, 4128, 4410, 4789],
    'PPE_Net': [3900, 4150, 4350, 4570, 4790],
    'Total_Assets': [7200, 7765, 8478, 8980, 9579],
    'Accounts_Payable': [1010, 1080, 1150, 1210, 1250],
    'Short_Term_Debt': [2900, 2750, 2600, 2450, 2300],
    'Total_Current_Liabilities': [3910, 3830, 3750, 3660, 3550],
    'Total_Liabilities': [3910, 3830, 3750, 3660, 3550],
    'Total_Equity': [3290, 3935, 4728, 5320, 6029],
    # Cash Flow (£ thousands)
    'CFO': [1050, 1290, 1480, 1750, 2050],
    'Capex': [-350, -380, -400, -420, -440],
    'CFF': [-180, -150, -150, -150, -150],
}

df = pd.DataFrame(data)
df.to_csv('/home/claude/python_project/financial_statements.csv', index=False)
print(df.T)
