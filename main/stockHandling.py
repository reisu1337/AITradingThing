import yfinance as yf
import pandas
import os
from os.path import exists
from datetime import datetime

today = datetime.today()
d4 = today.strftime("%b-%d-%Y")


def collectData(ticker):
    data = yf.download(tickers=ticker, period="1y", interval="1d", rounding=True, progress=False, show_errors=False)
    if data.empty:
        return False
    path = os.path.join(os.path.dirname(__file__), f"{d4 + ticker}.csv")
    pandas.DataFrame.to_csv(data, path)
    return True


def retrieveData(ticker):
    if not exists(os.path.dirname(__file__) + "\\" + d4 + ticker + ".csv"):
        if not collectData(ticker):
            return "Stock Not Retrieved"
    df = pandas.read_csv(os.path.dirname(__file__) + "\\" + d4 + ticker + ".csv")
    return df


def clearCache():
    path = os.fsencode(os.path.dirname(__file__))
    for file in os.listdir(path):
        filename = os.fsencode(file)
        if filename.endswith(bytes(".csv", "utf-8")):
            if not filename.startswith(bytes(d4, "utf-8")):
                os.remove(file)


if __name__ == "__main__":
    print(retrieveData("GOOGL"))
    clearCache()
