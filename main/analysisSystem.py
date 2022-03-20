import numpy as np

from main import stockHandling as sh
from sklearn import linear_model
import pandas as pd
import datetime as dt


def regLine(ticker):
    sh.retrieveData(ticker)
    df = sh.stock.getDataFrame(sh.stock)
    df["Date"] = pd.to_datetime(df["Date"])
    df['Date'] = df['Date'].map(dt.datetime.toordinal)
    dataX = np.array(df['Date'])
    dataY = np.array(df["Close"])

    dataXTrain = dataX[:-20].reshape(-1, 1)
    dataXTest = dataX[:].reshape(-1, 1)
    dataYTrain = dataY[:-20].reshape(-1, 1)

    regr = linear_model.LinearRegression()

    regr.fit(dataXTrain, dataYTrain)

    dataYPred = regr.predict(dataXTest)
    dtDataXTest = []
    for i in dataXTest:
        data = dt.datetime.fromordinal(i[0]).date().strftime("%Y-%m-%d")
        dtDataXTest.append(data)

    return dtDataXTest, dataYPred


if __name__ == "__main__":
    regLine("googl")
