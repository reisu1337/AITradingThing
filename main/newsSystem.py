import requests
import datetime
import json

monthAgo = datetime.datetime.now() - datetime.timedelta(days=29)

if __name__ == "__main__":

    url = ('https://newsapi.org/v2/everything?'
           'q=Apple&'
           f'from={monthAgo}&'
           'sortBy=popularity&' 
           'pageSize=3&'
           'apiKey=9ccce57e61324a3b999000d3da8e2ea8')

    response = requests.get(url)

