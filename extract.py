from config import key, stocks
import requests
import time
import csv

stock_name = ""

for stock in stocks:
    stocks_url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=120&apiKey={key}"
    data = requests.get(stocks_url)

    if stock_name != stock:
        stock_name = stock        
        csv_name = stock + ".csv"
        print(csv_name)
        with open(csv_name, 'w', newline='') as csvfile:
            fieldnames = ['date', 'closing']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            results = data.json()["results"]
            for result in results:
                print(f"stock: {stock}, date: {time.strftime('%Y-%m-%d', time.localtime(int(int(result['t'])/1000)))} closing: {result['c']}")
                writer.writerow({'date': time.strftime('%Y-%m-%d', time.localtime(int(int(result['t'])/1000))), 'closing': result['c']})
