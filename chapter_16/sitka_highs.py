# -*- coding: utf-8 -*-
import csv
from datetime import  datetime
from matplotlib import pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader) # read one string from object f
    print(head_row)

    # Find out all titles and their position in a list
    #enumerate() returns index and value of every item of the list
    # for index, column_header in enumerate(head_row):
    #     print(index, column_header)

    #Geting TMAX only (index - 5)
    dates, highs, lows = [], [], []
    for row in reader:
        concurrent_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(concurrent_date)
        highs.append(high)
        lows.append(low)

# print(highs)
#Plotting Data on a diagram
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

#Formating diagram
plt.title("Daily high and low temperature - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # show dates in diagonal way
plt.ylabel('Temperature (F)', fontsize=16)
ax.set_ylim(0, 130)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
