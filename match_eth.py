import csv
import pandas as pd
import numpy as np

df1 = pd.read_csv('Ethbal01.csv' , usecols = ["address"])
df1np = np.array(df1["address"])

ef1 = pd.read_csv('ether_addresses.csv' , usecols = ["address"])
ef1np = np.array(df1["address"])
print(ef1np)

match = np.intersect1d(ef1np, df1np)
if match.size> 0:
	print(match.size)
	#data = [match, filename]
	with open("res.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow(match)
			
print(match)