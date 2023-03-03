
import csv

with open("datasetT5.csv", 'r') as csvfile:
    rows = csv.reader(csvfile)
    for data in rows:
        print(data)