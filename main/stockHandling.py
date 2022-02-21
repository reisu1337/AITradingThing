import pandas as pd
import plotly.graph_objs as go
import yfinance as yf
import plotly.express as px
import pandas
import os
from os.path import exists
from datetime import datetime


def collectData(ticker):
    today = datetime.today()
    d4 = today.strftime("%b-%d-%Y")
    data = yf.download(tickers=ticker, period="1y", interval="1d", rounding=True)
    path = os.path.join(os.path.dirname(__file__), f"{d4+ticker}.csv")
    pandas.DataFrame.to_csv(data, path)

def createGraph(ticker):
    today = datetime.today()
    d4 = today.strftime("%b-%d-%Y")
    if not exists(os.path.dirname(__file__)+"\\"+d4+ticker+".csv"):
        collectData(ticker)
    df = pandas.read_csv(os.path.dirname(__file__)+"\\"+d4+ticker+".csv")
    print(df)


if __name__ == "__main__":
    createGraph("GOOGL")
