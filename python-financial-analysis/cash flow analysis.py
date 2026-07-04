"""
cash_flow_analysis.py
Analyzes free cash flow and cash flow trends from financial statement data.
"""
import pandas as pd


def analyze_cash_flow(df: pd.DataFrame) -> pd.DataFrame:
    cf = pd.DataFrame()
    cf['Year'] = df['Year']
    cf['CFO'] = df['CFO']
    cf['Capex'] = df['Capex']
    cf['Free_Cash_Flow'] = df['CFO'] + df['Capex']
    cf['CFF'] = df['CFF']
    cf['Net_Cash_Change'] = cf['CFO'] + cf['Capex'] + cf['CFF']
    cf['FCF_Margin_%'] = (cf['Free_Cash_Flow'] / df['Revenue'] * 100).round(1)
    cf['FCF_to_Net_Income_%'] = (cf['Free_Cash_Flow'] / df['Net_Income'] * 100).round(1)
    cf['Cash_Balance'] = df['Cash']
    return cf


if __name__ == '__main__':
    df = pd.read_csv('/home/claude/python_project/financial_statements.csv')
    cf = analyze_cash_flow(df)
    cf.to_csv('/home/claude/python_project/cash_flow_analysis_output.csv', index=False)
    pd.set_option('display.width', 200)
    print(cf.T)
