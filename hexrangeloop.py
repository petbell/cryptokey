# this creates addresses from a loop of hex private key and saves in an excel file.
# after that, the excel file is loaded into another py script (testbalance.py) to check for balances.
from eth_account import Account
from openpyxl import Workbook

wb_name = "large5pk.xlsx"
wb = Workbook()
ws = wb.active

for j in range( 28, 40):
	headers = ['PRIVATE KEY', 'ADDRESS']
	ws = wb.active
	ws.append(headers)
	wbname = "pk" + str(j)+ ".xlsx"
	print ("Present file is " + wbname)
	private_key ="ffe8b2eabec7247b085c243d6c529501a166d47e484cc1454d60c930c6bc985"
	for i in range(1,500001):
		
		i = int(private_key, 16)
		i += 1
		print (hex(i))
		private_key = hex(i)
	
		acct = Account.from_key(private_key)
		print ("address :", acct.address)

		row = [private_key,acct.address]
		ws.append(row)
	wb.save(filename = wb_name)
	ws = []
print("finito, God no go shame us!!")

	

