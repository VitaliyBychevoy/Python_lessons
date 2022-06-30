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
filename_Sitka = 'data/sitka_weather_2018_simple.csv'
filename_dv = 'data/death_valley_2018_simple.csv'

with open(filename_Sitka) as fS:
    reader = csv.reader(fS)
    head_row = next(reader)

    print("Sitka`s column")
    for i, value in enumerate(head_row):
        print(i, value)

    dates_for_Sitka, temper_max_for_Sitka, temper_min_for_Sitka  = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            temper_max = float(row[5])
            temper_min = float(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_for_Sitka.append(current_date)
            temper_min_for_Sitka.append(temper_min)
            temper_max_for_Sitka.append(temper_max)
fS.close()
print("\n")
with open(filename_dv) as fdv:
    reader_dv = csv.reader(fdv)
    head_row = next(reader_dv)

    print("DV`s column")
    for i, val in enumerate(head_row):
        print(i, val)

    dates_for_dv, temper_max_for_dv, temper_min_for_dv = [], [], []
    for row in reader_dv:
        current_date_dv = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            temper_max_dv = float(row[4])
            temper_min_dv = float(row[5])
        except ValueError:
            print(f"Missing data for {current_date_dv}")
        else:
            dates_for_dv.append(current_date_dv)
            temper_max_for_dv.append(temper_max_dv)
            temper_min_for_dv.append(temper_min_dv)
fdv.close()


plt.style.use('seaborn')
line_Sitka_max = plt.plot(dates_for_Sitka, temper_max_for_Sitka, '-', color='g')
line_Sitka_min = plt.plot(dates_for_Sitka, temper_min_for_Sitka, '-', color='g')
line_dv_max = plt.plot(dates_for_dv, temper_max_for_dv, color='r')
line_dv_min = plt.plot(dates_for_dv, temper_min_for_dv, color='r')
plt.fill_between(dates_for_Sitka, temper_max_for_Sitka, temper_min_for_Sitka,
                 color='b', alpha=0.5)
plt.fill_between(dates_for_dv, temper_max_for_dv,temper_min_for_dv, color='y',
                 alpha=0.5)
plt.title("Sitka and Death Valley.")
plt.ylabel('Temper', fontsize=16)
plt.xlabel('Time', fontsize=16)
plt.show()