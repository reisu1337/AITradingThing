from matplotlib import pyplot as plt
from main import stockHandling as sh, analysisSystem as anas
from datetime import datetime
import os
from pathlib import Path
import yfinance as yf

today = datetime.today()
d4 = today.strftime("%b-%d-%Y")
path = Path(os.path.dirname(__file__)).parent.absolute()


def main(ticker):
    sh.retrieveData(ticker)
    df = sh.stock.getDataFrame(sh.stock)
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"])
    ax.set(xlabel='Time', ylabel='Price ($)',
           title=f"Graph - {ticker.upper()}")
    ax.grid()

    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    x, y = anas.regLine(ticker)
    plt.plot(x, y, color="red")
    plt.savefig(f"{d4}{ticker}graph.png")


if __name__ == "__main__":
    main("googl")
