import csv

filename= input("Enter csv file \n")
address = '0x57D3D913A3Ca5a7d25A5c072eA2079e5701A5E1A'
address = address.lower()
#input("Give me the address?\n")

csv_file = csv.reader(open("Ethbal" +filename +".csv", "r"), delimiter = ",")

print(str(address))
print(address)

for row in csv_file:
	#use this print to check if you are querying the right row index for the if statement below
	#print(row[0])
	
	if str(address) == row[0]:
		print (row)
	#else:
		#print("record not found")