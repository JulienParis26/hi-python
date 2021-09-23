import json
import csv

with open('./ex01_json2csv/menu.json') as json_file:
    data = json.load(json_file)
 
menu = data['menu']

toCsv = open('./ex01_json2csv/menu.csv', 'w')

csv_writer = csv.writer(toCsv)

count = 0
 
for std in menu:
    if count == 0:

        header = std.keys()
        csv_writer.writerow(header)
        count += 1
        
    csv_writer.writerow(std.values())
 
toCsv.close()