from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import datetime

# Create stock data client
client = StockHistoricalDataClient()

# Creating request parameter object
requestParams = StockBarsRequest(
    symbol_or_symbols = ["USD"],
    timeframe = TimeFrame.Day,
    start = datetime(2025, 4, 20),
    end = datetime(2025, 4, 21)
)

# Retrieve stock bars in a data frame
stockBars = client.get_stock_bars(requestParams)

# Convert to dataframe 
stockBars.df