# Tesla DCF Valuation 🚗💰

## Overview  
This project presents a **Discounted Cash Flow (DCF)** valuation for **Tesla (TSLA)** to estimate its intrinsic stock value based on projected future cash flows, the Weighted Average Cost of Capital (WACC), and the terminal growth rate.

## Key Findings  
- **Estimated fair value per share:** **$65.18**  
- **Market price (as of the project date):** **$112.00**  
- **WACC used:** **8%**  
- **Assumed long-term growth rate:** **3-5%**  

## Methodology  
The following steps were taken to perform the DCF valuation:

1. **Download Tesla’s financial data:**  
   - Used the `yfinance` library to download Tesla’s financial data (income statement, balance sheet, and cash flow statement).
   - The data was saved to CSV files for later reference.

2. **Project future cash flows (5 years):**  
   - Based on Tesla’s past performance, future cash flows were projected to grow at 15-20% annually over the next 5 years.
   - These projections were used as inputs for the DCF calculation.

3. **Discount future cash flows using WACC:**  
   - A **WACC of 8%** was applied to discount the projected future cash flows back to their present value.
   - The present value of each cash flow was calculated for the first 5 years.

4. **Calculate terminal value:**  
   - The **Gordon Growth model** was used to estimate the terminal value based on Tesla’s final year of projected cash flow, with a growth rate of **3%** (a conservative long-term growth rate).
   - The terminal value was then discounted back to present value.

5. **Sum up present values to determine intrinsic value:**  
   - The total present value of future cash flows (from the 5 years) and the present value of the terminal value were added together.
   - The intrinsic value per share was calculated by dividing the total present value by the number of shares outstanding.

## Files  
- `tesla_dcf.xlsx` → Full DCF model in Excel format  
- `tesla_dcf.py` → Python script used for DCF valuation  
- `tesla_financials.py` → Python script to download Tesla's financial data from Yahoo Finance  
- `README.md` → Project summary  

## Next Steps  
- Improve growth assumptions by factoring in **macroeconomic trends** and **industry-specific developments**.
- Explore other **valuation methods** (such as **Comparables** and **Precedent Transactions**) to cross-check results.
- Refine the **assumptions for future growth** based on additional research or updated financial reports.

## Installation & Usage  
### Prerequisites
Ensure you have **Python 3** installed and the required packages:
- `yfinance` for downloading financial data
- `pandas` for data manipulation
- `numpy` for numerical calculations

You can install these using pip:
```bash
pip install yfinance pandas numpy



### Breakdown of Sections:
- **Overview:** Briefly explains the purpose of the project and what it does.
- **Key Findings:** Highlights the result of the project, such as the intrinsic value per share and the WACC used.
- **Methodology:** Details the steps you took to gather financial data, make projections, and run the DCF calculation.
- **Files:** Lists all the files in the repository, including the Python scripts and Excel file.
- **Next Steps:** Suggests future improvements and how the project could be expanded.
- **Installation & Usage:** Describes how to run the project, including prerequisites and instructions.
- **Disclaimer:** Adds a note that the valuation is based on assumptions and should be treated as an estimate.

### Next Steps:
- You can create a new file called `README.md` in your local project folder.
- Paste the content above into that file and then follow the steps I shared earlier to upload it to GitHub.

Let me know if you need further adjustments!

