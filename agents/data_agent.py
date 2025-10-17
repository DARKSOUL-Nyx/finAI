import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period="1y"):
    try:
        data = yf.download(ticker, period=period)
        data.reset_index(inplace=True)
        data.to_csv("data/stock_data.csv", index=False)
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return pd.DataFrame()
