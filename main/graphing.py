from matplotlib import pyplot as plt
from main import stockHandling as sh
import yfinance as yf



def main(ticker):
    sh.retrieveData(ticker)
    df = sh.stock.getDataFrame(sh.stock)
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"])
    ax.set(xlabel='Time', ylabel='Price ($)',
           title=f"Graph - {ticker.upper()}")
    ax.grid()

    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    plt.savefig(f"{ticker}graph.png")


if __name__ == "__main__":
    main("googl")
