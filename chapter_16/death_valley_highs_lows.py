# -*- coding: utf-8 -*-
import csv
from datetime import  datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Geting TMAX only (index - 5)
    dates, highs, lows = [], [], []
    for row in reader:
        concurrent_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {concurrent_date}")
        else:
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
plt.title("Daily high and low temperature - 2018\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # show dates in diagonal way
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()