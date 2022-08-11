import csv
import pandas as pd

#df = pd.read_csv("chunk41.csv")

#df1= df.tail(5)
#print(df1)

chris ="0xcB44b2B501C1e5ee90B13D794dff589B0c39Df6B"
chris_low = [chris.lower()]

#print(chris_low)

with open('Ethbal02.csv',  'a') as f:
	writer = csv.writer(f)
	writer.writerow(chris_low)
print ('data appended')