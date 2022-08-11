import csv
import pandas as pd
import numpy as np


for g in range(1,4):
	filename = 'pk' +str(g)+ '.csv'
	#headerList = ['privatekey', 'address']
	mine = pd.read_csv(filename,  usecols= ["address"])
	#mine.to_csv("pk4.csv", header= headerList, index ="False")
	#print (mine.head(5))
	print("minenp : ")
	minenp = np.array(mine["address"])
	print(minenp)

	#print(minenp)


	for i in range(1,6):
		#df1 = pd.read_csv('chunk' +str(i) + '.csv' , usecols = ["address"])
		df1 = pd.read_csv('Ethbal0' +str(i) + '.csv' , usecols = ["address"])
		df1np = np.array(df1["address"])
		print(df1np)
		print(type(df1np))
		
		
		match = np.intersect1d(minenp, df1np)
		if match.size> 0:
			print(match.size)
			data = [match, filename]
			with open("results1.csv", 'a') as file:
				writer = csv.writer(file)
				writer.writerow(data)
			
		print(match)
		print("iterations left: " +str(5 - i)+ ". Current file is: " +str(g))
	print("Next file is: " +str(g+1))


