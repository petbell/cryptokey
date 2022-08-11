# this creates addresses from a loop of hex private key and saves in an excel file.
# after that, the excel file is loaded into another py script (testbalance.py) to check for balances.
# on windows, first intall bitarray, then web3 for eth-accout to work
from eth_account import Account
#from openpyxl import Workbook
import secrets
import csv

#wb_name = "pk2.xlsx"
#wb = Workbook()
#ws = wb.active
header = ['privatekey', 'address']

priv = secrets.token_hex(32)
print ("processing......")
print ("page running")
print (".......")
print (".......")
print ("processing......")
print ("processing......")
print ("page running")
print (".......")
print (".......")
print ("processing......")
print ("processing......")
print ("page running")
print (".......")
print (".......")
print ("processing......")




private_key = priv
for i in range(1,23674367):
	i = int(private_key, 16)
	i += 1 #20988936657440586486151264256610222593863921
	print (hex(i))
	private_key = hex(i)
	
	acct = Account.from_key(private_key)
	print ("address :", acct.address)

	row = [private_key,acct.address.lower()]
	#ws.append(row)
	with open('pk3.csv',  'a') as f:
		writer = csv.writer(f)
		#writer.writerow(header)
		writer.writerow(row)
#wb.save(filename = wb_name)
print("finito, God no go shame us!!")

	

