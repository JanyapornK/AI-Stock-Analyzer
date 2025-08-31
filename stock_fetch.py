import pandas as pd
import json
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.widgets as widgets
import requests
import os
from dotenv import load_dotenv

class StockAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Please set ALPHAVANTAGE_API_KEY in your .env file.")

    def get_stock_data(self, stock, market):
        if market == "NASDAQ":
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize=compact&apikey={self.api_key}"
        else:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}.{market}&outputsize=compact&apikey={self.api_key}"
        r = requests.get(url)
        data = r.json()
        return data
    
class StockAnalyzer:
    def __init__(self):
        pass

    def json_to_dataframe(self, json_data, ticker, market):
        print(json_data)
        time_series_data = json_data['Time Series (Daily)']
        df_data =[]

        for date_str, values in time_series_data.items():
            data_row = {'date': date_str}
            for key, value in values.items():
                new_key = key.split('. ')[1]
                data_row[new_key] = float(value)
            df_data.append(data_row)
        
        df = pd.DataFrame(df_data)
        df['date'] = pd.to_datetime(df['date'])

        eastern = pytz.timezone('US/Eastern')
        ist = pytz.timezone('Asia/Kolkata')

        df['date'] = df['date'].dt.tz_localize(eastern).dt.tz_convert(ist)
        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['stock'] = ticker
        df['market'] = market

        df = df.set_index('date')
        return df
    
    def plot_stock_data(self, df, ticker, market, image_path):
        plt.figure(figsize=(16,10))

        #Plotting Close Price
        plt.subplot(3,1,1)
        plt.plot(pd.to_datetime(df.index), df['close'], label=f'{ticker} Close Price ({market})', color='blue')
        plt.title(f'{ticker} Stock Performance ({market})')
        plt.xlabel('Date (IST)')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)

        #Enhanced Data Formatting
        for ax in plt.gcf().axes:
            #Major ticks every month, minor ticks every week
            ax.xaxis.set_major_locator(mdates.MonthLocator())

        
        cursor = widgets.Cursor(plt.gca(), color='red', linewidth=1)

        plt.tight_layout()
        plt.savefig(image_path)
        plt.show()