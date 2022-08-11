import csv
from openpyxl import Workbook

file_name = input("load csv file: ")
wb = Workbook()
ws = wb.active

with open(file_name + '.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		ws.append(row)
		
wb.save(file_name + '.xlsx')

print(file_name+ '.csv successfully converted to '+file_name +'.xlsx' )