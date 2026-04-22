
import yfinance as yf
import pandas as pd  # <--- Added this to define 'pd'

def checkvalue(stock):
    ticker = yf.Ticker(stock)
    print(f"Stock Name: {stock}")
    # Fetch the growth estimates table
    df = ticker.growth_estimates
    if df is not None and not df.empty:
        try:
            # Based on your previous output:
            # Row index is '+1y', Column name is 'stockTrend'
            next_year_growth = df.loc['+1y', 'stockTrend']
            fg = 0
            # Check if the value is a valid number (not NaN)
            if not pd.isna(next_year_growth):
                print(f"Growth Estimate for Next Year: {next_year_growth * 100:.2f}%")
                fg = next_year_growth * 100
            else:
                print("Next Year growth estimate is currently NaN for this ticker.")

        except KeyError:
            print("Structure mismatch. Available columns:", df.columns.tolist())
    else:
        print("Table is empty. Ensure you are connected to the internet.")
    
    info = ticker.info
    # Extract specific metrics
    price = info.get('currentPrice')
    pe_ratio = info.get('trailingPE')
    div_yield = info.get('dividendYield')
    dy = div_yield
    # Format Dividend Yield as percentage (e.g., 0.015 -> 1.50%)
    if div_yield:
        print(f"Dividend Yield: {div_yield * 100:.2f}%")
    else:
        print("Dividend Yield: N/A")

    result = (fg + dy)/pe_ratio
    expected_price = round(price * result, 2)
    difference_percentage = round((price - expected_price)/((expected_price + price)/2)*100,2)
    print(f"Future Growth: {round(fg,2)} \nDividend Yield: {dy} \nP/E Ratio: {round(pe_ratio,2)} \
          \nResult: {round(result,2)} \nCurrent Price: {price}\nExpected Price: {expected_price} \
          \nPercentage Difference: {difference_percentage}%")

stock = input("Enter name of stock: ")
checkvalue(stock)