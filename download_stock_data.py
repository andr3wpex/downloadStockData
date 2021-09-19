""" 
The choice of the below methods for downloading stock data would produce
identical data, but for different date ranges due to yf being offset by
one business day. Different methods require different start and end parameters. 
"""

import time
import datetime
import pandas as pd

start = "2021-01-01"
end = "2021-01-31"

# Method 1: using a query string to download stock data 

ticker = 'AAPL'
period1 = int(time.mktime(datetime.datetime(int(start.split("-")[0]), int(start.split("-")[1]), int(start.split("-")[2]), 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(int(end.split("-")[0]), int(end.split("-")[1]), int(end.split("-")[2]), 23, 59).timetuple()))
interval = '1d' # 1d, 1wk, 1m

query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

df_link = pd.read_csv(query_string, index_col='Date')

# Methon 2: leveraging the yf library (yf.download method)

import yfinance as yf
df_yf = yf.download(ticker, start=start, end=end, group_by="ticker")

print("\n\n-----query string-----")
print("using query strings will return the exact date ranges:")
print(df_link.head(3))
print(df_link.tail(3))

print("\n\n-----yf.download-----")
print("the yf library with the same parameters shifts the dataset by one trading day which may be more than 1 calendar day")
print(df_yf.head(3))
print(df_yf.tail(3))

# using yf, includes the preceeding working day
print(df_link.shape, df_yf.shape)