import pandas as pd
import csv

olddf = pd.read_csv('ether_addresses.csv', usecols= ['address'])
print(olddf.head(5))


newdf = pd.read_csv('ether_addresses1.csv', usecols = ['address'])
print(newdf.head(5))

finaldf = olddf + newdf
finaldf = list(set(finaldf))
print(finaldf)
with open('feth_addresses.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(finaldf)
