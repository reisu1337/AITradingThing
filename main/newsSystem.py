import datetime

import requests
import yfinance as yf

monthAgo = datetime.datetime.now() - datetime.timedelta(days=29)


def getNews(ticker):
    companyName = yf.Ticker(ticker).info["longName"]

    url = ('https://newsapi.org/v2/everything?'
           f'q={companyName}&'
           f'from={monthAgo}&'
           'sortBy=popularity&'
           'pageSize=3&'
           'apiKey=9ccce57e61324a3b999000d3da8e2ea8')

    response = requests.get(url)
    h1 = response.json()["articles"][0]["title"]
    h2 = response.json()["articles"][1]["title"]
    h3 = response.json()["articles"][2]["title"]

    l1 = response.json()["articles"][0]["url"]
    l2 = response.json()["articles"][1]["url"]
    l3 = response.json()["articles"][2]["url"]

    return h1, h2, h3, l1, l2, l3


def getMoreNewsLink(ticker):
    companyName = yf.Ticker(ticker).info["longName"]
    url = f"https://news.google.com/search?q={companyName}"
    return url


if __name__ == "__main__":
    getNews("aapl")
