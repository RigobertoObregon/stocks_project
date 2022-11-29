from config import key
import requests
import time

stocks = ["GOOG", "AMZN", "COUR", "NFLX", "META"]

for stock in stocks:
    stocks_url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=120&apiKey={key}"
    data = requests.get(stocks_url)

    results = data.json()["results"]
    for result in results:
        print(f"stock: {stock}, date: {int(int(result['t']))} closing: {result['c']}")
        #print(f"stock: {stock}, date: {time.strftime('%y-%m-%d', int(int(result['t'])/1000))} closing: {result['c']}")

#print(time.strftime('%y-%m-%d', ))
