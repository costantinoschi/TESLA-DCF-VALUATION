import yfinance as yf

# Step 1: Download Tesla financials
tsla = yf.Ticker("TSLA")
income_statement = tsla.financials
balance_sheet = tsla.balance_sheet
cash_flow = tsla.cashflow

# Save to CSV (optional)
income_statement.to_csv("tesla_income_statement.csv")
balance_sheet.to_csv("tesla_balance_sheet.csv")
cash_flow.to_csv("tesla_cash_flow.csv")

# Step 2: Define constants for DCF model
discount_rate = 0.08  # 8% WACC
terminal_growth_rate = 0.04  # 4% long-term growth rate after 5 years
shares_outstanding = tsla.info.get('sharesOutstanding', 0)  # Get shares outstanding from the info

# Check if the shares outstanding value was retrieved correctly
print(f"Shares Outstanding: {shares_outstanding}")

# Step 3: Projected future cash flows (in billions)
future_cash_flows = [10, 11.5, 13.2, 15.2, 17.5]  # in billions of USD

# Step 4: Discount future cash flows to present value
present_value_of_cash_flows = 0
for year, cash_flow in enumerate(future_cash_flows, 1):
    discounted_cash_flow = cash_flow / (1 + discount_rate) ** year
    present_value_of_cash_flows += discounted_cash_flow
    print(f"Year {year}: Cash Flow = {cash_flow}B, Discounted CF = {discounted_cash_flow:.2f}B")

# Step 5: Calculate terminal value using Gordon Growth Model
terminal_value = future_cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
print(f"Terminal Value: ${terminal_value:.2f}B")

# Step 6: Discount terminal value to present value
present_value_of_terminal_value = terminal_value / (1 + discount_rate) ** len(future_cash_flows)
print(f"Present Value of Terminal Value: ${present_value_of_terminal_value:.2f}B")

# Step 7: Calculate total present value
total_present_value = present_value_of_cash_flows + present_value_of_terminal_value
print(f"Total Present Value: ${total_present_value:.2f}B")

# Step 8: Calculate intrinsic value per share
# Check that total present value and shares outstanding are correct before calculating
if shares_outstanding > 0 and total_present_value > 0:  # Ensure the number of shares is valid
    intrinsic_value_per_share = total_present_value * 1e9 / shares_outstanding  # Multiply by 1e9 to convert to dollars from billions
    print(f"Intrinsic Value per Share: ${intrinsic_value_per_share:.2f}")
else:
    print(f"Error: Invalid shares outstanding value or total present value is too low.")


# Step 8: Calculate intrinsic value per share
if shares_outstanding > 0:  # Ensure the number of shares is valid
    intrinsic_value_per_share = total_present_value / shares_outstanding
    print(f"Intrinsic Value per Share: ${intrinsic_value_per_share:.2f}")
else:
    print("Error: Invalid shares outstanding value.")

