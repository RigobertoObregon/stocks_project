from config import key, stocks
import requests
import time
import csv

def extract():
    '''
    Function name: extract
    It does not receive parameters.
    It connects to api.polygon.io API to get daily stock information.
    Then generates a csv file for each stock contained in a list.
    '''

    stock_name = ""

    # for each stock name contained in config file, get stock information 
    for stock in stocks:
        # getting the data from the API
        stocks_url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=120&apiKey={key}"
        data = requests.get(stocks_url)

        if stock_name != stock:
            stock_name = stock        
            csv_name = stock + ".csv"
            print(csv_name)

            # create a file for each stock name
            with open(csv_name, 'w', newline='') as csvfile:
                # setting up the header for the file
                fieldnames = ['date', 'closing']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                # writting the data from the data list to the file
                results = data.json()["results"]
                # for each dict object in data list
                for result in results:
                    writer.writerow({'date': time.strftime('%Y-%m-%d', time.localtime(int(int(result['t'])/1000))), 'closing': result['c']})

# calling extract() function
e = extract()

#optionally, we can see the comment for the extract() function
#print(extract.__doc__)