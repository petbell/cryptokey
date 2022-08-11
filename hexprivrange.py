# this creates addresses from a loop of hex private key and saves in an excel file.
# after that, the excel file is loaded into another py script (testbalance.py) to check for balances.
from eth_account import Account
from openpyxl import Workbook
import secrets
import csv

wb_name = "pk2.xlsx"
wb = Workbook()
ws = wb.active

priv = "0xbe46ac1eb4d387eef3bb0efc0f5159978e1ce4dd0c85b44b0c588b24eb6751bd"

#secrets.token_hex(32)

private_key = priv
for i in range(1,1000001):
	i = int(private_key, 16)
	i += 1
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

	

