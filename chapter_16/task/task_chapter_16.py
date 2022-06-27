# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from matplotlib import pyplot as plt

"""
print("\n\t 16.1 Осадки в Ситке.")
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, columns in enumerate(header_row):
        print(index, columns)

    dates, prcp = [], []
    for row in reader:
        concurrent_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            prcp_item = float(row[3])
        except ValueError:
            print(f"Missing data for {concurrent_date}")
        else:
            dates.append(concurrent_date)
            prcp.append(prcp_item)

#Plotting Data on a diagram
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcp, c='red', alpha=0.7)

#Formating diagram
plt.title("Осадки", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Уровень осадков', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
"""
print("\n\t 16.3 Осадки в Cан Франсиско.")


filename_San_Fransisco = "data/San_Fransisco-2022-01-01_2022-06-22.csv"

with open(filename_San_Fransisco) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column in enumerate(header_row):
        #print(index, column)

    dates, temp_max, temp_min = [], [], []
    for row in reader:
        concurrent_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            temp = float(row[4])
            temp_m = float(row[5])
        except ValueError:
            print(f"Missing data for {concurrent_date}")
        else:
            dates.append(concurrent_date)
            temp_max.append(temp)
            temp_min.append(temp_m)
    f.close()

filename_Sitka = 'data/sitka_weather_2018_simple.csv'
with open(filename_San_Fransisco) as d:
    reader_1 = csv.reader(d)
    header_row = next(reader_1)
    dates_Sitka, temp_max_Sitka, temp_min_Sitka = [], [], []
    for row in reader_1:
        concurrent_date_2 = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            temp_1 = float(row[4])
            temp_2 = float(row[5])
        except ValueError:
            print(f"Missing data for {concurrent_date_2}")
        else:
            dates_Sitka.append(concurrent_date_2)
            temp_max_Sitka.append(temp_1)
            temp_min_Sitka.append(temp_2)
    d.close()
filename_dv = 'data/death_valley_2018_simple.csv'
with open(filename_dv) as h:
    reader_dv = csv.reader(h)
    header_row = next(reader_dv)
    dates_dv, temp_max_dv, temp_min_dv = [], [], []
    for row in reader_dv:
        concurrent_date_dv = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            temp_1_dv = float(row[4])
            temp_2_dv = float(row[5])
        except ValueError:
            print(f"Missing data for {concurrent_date_dv}")
        else:
            dates_Sitka.append(concurrent_date_dv)
            temp_max_Sitka.append(temp_1_dv)
            temp_min_Sitka.append(temp_2_dv)
    h.close()
#Plotting Data on a diagram
plt.style.use('seaborn')
fig, ax = plt.subplots()

#San_Fransisco
#ax.plot(dates, temp_max, c='red', alpha=0.7)
#ax.plot(dates, temp_min, c='red')
#plt.fill_between(dates, temp_max, temp_min, facecolor='red', alpha=0.2)

#Sitka
ax.plot(dates_Sitka, temp_max_Sitka, c='red')
ax.plot(dates_Sitka, temp_min_Sitka, c='red')
#plt.fill_between(dates_Sitka, temp_max_Sitka, temp_min_Sitka, facecolor='green', alpha=0.2)

#DV
ax.plot(dates_dv, temp_max_dv, c='blue', alpha=0.7)
ax.plot(dates_dv, temp_min_dv, c='yellow')


#Formating diagram
plt.title("Температура ", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Температура ', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()