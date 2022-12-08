from config import stocks
import csv
from datetime import datetime
import statistics
import matplotlib.pyplot as plt

stddevs = []

for stock in stocks:
    stock_data = []
    file_name = stock + ".csv"
    with open(file_name, "r") as infile:
        reader = csv.DictReader(infile)

        first = True
        week_values = []
        for row in reader:
            row["stock"] = stock
            row["week"] = datetime.strptime(row["date"], '%Y-%m-%d').isocalendar()[1]
            #print(row)
            new_week = int(datetime.strptime(row["date"], '%Y-%m-%d').isocalendar()[1])
            if first == True:
                first = False
                week_values.append(float(row["closing"]))
                week = new_week
            else:
                if new_week == week:
                    week_values.append(float(row["closing"]))
                else:
                    if len(week_values) > 1:
                        stddev = statistics.stdev(week_values)
                        stddevs.append({"stock":stock, "week":week, "stddev":stddev})
                    week_values = []
                    week = new_week

stock_number = 1
for stock in stocks:
    week = []
    stddev = []
    for s in stddevs:
        if s["stock"] == stock:
            week.append(s["week"])
            stddev.append(s["stddev"])
    plt.subplot(2, 3, stock_number)
    plt.plot(week, stddev, label = stock)
    plt.title(stock)
    plt.xlabel("Week")
    plt.ylabel("Std Dev")
    #plt.figure()
    stock_number += 1


plt.show()






