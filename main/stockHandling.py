import yfinance as yf
import pandas
import os
from os.path import exists
from datetime import datetime
from main import stockClass as sc

today = datetime.today()
d4 = today.strftime("%b-%d-%Y")

stock = sc.Stock
path = os.fsencode(os.path.dirname(__file__))


def collectData(ticker):
    data = yf.download(tickers=ticker, period="1y", interval="1d", rounding=True, progress=False, show_errors=False)
    if data.empty:
        return False
    path = os.path.join(os.path.dirname(__file__), f"{d4 + ticker}.csv")
    pandas.DataFrame.to_csv(data, path)
    return True


def clearCache():
    for file in os.listdir(path):
        filename = os.fsencode(file)
        if filename.endswith(bytes(".csv", "utf-8")):
            if not filename.startswith(bytes(d4, "utf-8")):
                os.remove(path + bytes("\\", "utf-8") + file)


def retrieveData(ticker):
    clearCache()
    if not exists(os.path.dirname(__file__) + "\\" + d4 + ticker + ".csv"):
        if not collectData(ticker):
            return False
    df = pandas.read_csv(os.path.dirname(__file__) + "\\" + d4 + ticker + ".csv")
    stock.setDataFrame(stock, df)
    return True


if __name__ == "__main__":
    retrieveData("GOOGL")
    print(stock.getDataFrame(stock))
