""" 
The choice of the below methods for downloading stock data would produce
identical data, but for different date ranges due to yf being offset by
one business day. Different methods require different begin and end parameters. 
"""

import time
import datetime
import pandas as pd
import yfinance as yf

class DataDownloader:
    def __init__(self, begin, end, ticker, interval='1d'):
        """ 
        Download stock data between "begin" and "end" dates
        for "ticker".
        The default granularity for 'interval' is daily.
        """
        
        self.begin = begin
        self.end = end
        self.ticker = ticker
        self.interval = interval
        
        self.begin_dt = int(time.mktime(datetime.datetime(int(self.begin.split("-")[0]), int(self.begin.split("-")[1]), int(self.begin.split("-")[2]), 23, 59).timetuple()))
        self.end_dt = int(time.mktime(datetime.datetime(int(self.end.split("-")[0]), int(self.end.split("-")[1]), int(self.end.split("-")[2]), 23, 59).timetuple()))
        self.query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{self.ticker}?period1={self.begin_dt}&period2={self.end_dt}&interval={self.interval}&events=history&includeAdjustedClose=true"
        
    def direct_link_df(self):
        # Method 1: using a query string to download stock data 
        df = pd.read_csv(self.query_string, index_col='Date')
        return df

    def yf_library_df(self):
        # Method 2: leveraging the yf library (yf.download method)
        df = yf.download(self.ticker, start=self.begin, end=self.end, group_by="ticker")
        return df

    def output_summary(self):
        print("\nticker: " + self.ticker + " was selected between " + self.begin + " and " + self.end)
        print("\n\n-----query string-----\n")
        print("using query strings will return the trading days in the date ranges:\n")
        print(self.direct_link_df().head())
        print(self.direct_link_df().tail())

        print("\n\n-----yf.download-----\n")
        print("the yf library with the same parameters shifts the dataset by one trading day which may be more than 1 calendar day:\n")
        print(self.yf_library_df().head())
        print(self.yf_library_df().tail())

        print("\nyf library would include the preceeding working day (out of the specified range)\n")
        print(self.direct_link_df().shape, self.yf_library_df().shape)

begin = "2021-01-01"
end = "2021-01-31"

# interval = 1d, 1wk, 1m, optional parameter

apple = DataDownloader(begin, end, 'AAPL')
microsoft = DataDownloader(begin, end, 'MSFT')

apple.output_summary()
print("\n__________________MICROSOFT__________________\n")
microsoft.output_summary()