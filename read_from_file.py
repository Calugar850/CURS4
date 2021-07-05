import json
import csv

if __name__ == '__main__':
    standings=[]
    with open('standings.json') as json_file:
        standings=json.load(json_file)
    print('standigs json',standings)

    with open('standings.csv') as csv_file:
        csv_rows=csv.reader(csv_file)
    print('standigs csv', standings)