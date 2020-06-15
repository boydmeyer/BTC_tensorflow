from binance.client import Client
import pandas as pd

api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

def get_full_data(SYMBOL):
    print("Retrieving all candles of " + str(SYMBOL) + "...")
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "10000 hours ago UTC")
    print(str(len(klines)) + " candles found...")
    df = pd.DataFrame(klines, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'IGNORE'])
    cols_to_drop = ['Open time', 'Close time', 'IGNORE']
    df = df[df.columns.drop(cols_to_drop)]
    return df

def get_last_60(SYMBOL):
    print("Retrieving last 60 candles of " + str(SYMBOL) + "...")
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "30 hours ago UTC")
    print(str(len(klines)) + " candles found...")
    df = pd.DataFrame(klines, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'IGNORE'])
    cols_to_drop = ['Open time', 'Close time', 'IGNORE']
    df = df[df.columns.drop(cols_to_drop)]
    return df.tail(60)
