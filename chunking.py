import csv
import pandas as pd

chunk_size = 1000000
batch_no = 1
headerList = ['privatekey', 'address']
for chunk in pd.read_csv ("pk1.csv", chunksize = chunk_size):
	chunk.to_csv('pn' + str(batch_no)+'.csv', index='false', header= headerList)
	df1 = pd.read_csv('pn' + str(batch_no)+'.csv', usecols = ["address"])
	print(df1.head(5))
	print(df1.tail(5))
	
	batch_no += 1