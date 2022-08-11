import csv
import pandas as pd
import numpy as np











for i in range(6,9):
	filename = "pk" +str(i)+ ".csv"
	#headerList = ['privatekey', 'address']
	mine = pd.read_csv(filename, usecols= ["address"])
	#mine.to_csv("pk4.csv", header= headerList, index ="False")
	#print (mine.head(5))
	
	minenp = np.array(mine["address"])
	#print(minenp)

	print(minenp)


	df1 = pd.read_csv('polygon_addresses.csv' , usecols = ["address"])
	df1np = np.array(df1["address"])
	#print(df1np)
		
	match = np.intersect1d(minenp, df1np)
	if match.size>0:
		print("matches are :" + str(match.size))
		data = [match, filename]
		with open("balancer.csv", 'a') as file:
			writer = csv.writer(file)
			writer.writerow(data)
			
	#print(match)
	#print("iterations left: " +str(20 - i))



