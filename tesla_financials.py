import yfinance as yf

# Download Tesla financials
tsla = yf.Ticker("TSLA")
income_statement = tsla.financials
balance_sheet = tsla.balance_sheet
cash_flow = tsla.cashflow

# Save to CSV
income_statement.to_csv("tesla_income_statement.csv")
balance_sheet.to_csv("tesla_balance_sheet.csv")
cash_flow.to_csv("tesla_cash_flow.csv")
