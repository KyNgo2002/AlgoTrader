from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# Loading environment variables
import os
from dotenv import load_dotenv

# Loading API and SECRET keys
load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Create stock data client
client = StockHistoricalDataClient(api_key = API_KEY, secret_key = SECRET_KEY)

# Creating request parameter object
requestParams = StockBarsRequest(
    symbol_or_symbols = ["AAPL"],
    timeframe = TimeFrame.Day,
    start = datetime(2022, 9, 1),
    end = datetime(2022, 10, 1)
)

# Retrieve stock bars in a data frame
stockBars = client.get_stock_bars(requestParams)

# Convert to dataframe 
print(stockBars.df)