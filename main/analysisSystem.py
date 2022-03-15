from main import stockHandling as sh
from sklearn import linear_model
import pandas as pd
import datetime as dt


def regLine(ticker):
    sh.retrieveData(ticker)
    df = sh.stock.getDataFrame(sh.stock)
    print(df)
    df["Date"] = pd.to_datetime(df["Date"])
    df['Date'] = df['Date'].map(dt.datetime.toordinal)
    dataX = df['Date']
    dataY = df["Close"]

    dataXTrain = dataX[:-20]
    dataXTest = dataX[-20:]
    dataYTrain = dataY[:-20]

    regr = linear_model.LinearRegression()

    regr.fit([dataXTrain], [dataYTrain])

    dataYPred = regr.predict(dataXTest)
    return dataXTest, dataYPred

if __name__ == "__main__":
    regLine("googl")