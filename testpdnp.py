import numpy as np
import pandas as pd
import csv
import openpyxl

chris =" 0xe2C544c76b00dFc2207D6b5340e05bf855095455"
chris_low = [chris.lower()]

print(chris_low)


for i in range(1,15):
	
	df1 = pd.read_csv( 'chunk' +str(i)+ '.csv')

	
	set_chris = set(chris_low)

	setdf1 = set(df1['address'])

	#print(set_chris)

	edey = set_chris.intersection(setdf1)
	print (edey)
	# " is present in the file, chunk" +str(i)+ ".csv")


	
	