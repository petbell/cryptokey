#this code creates a new excel file with headers then adds eth pks and addresses to it.
# to add more data, use the privrandom_load.py to append to the existing file.
from eth_account import Account
import secrets
from openpyxl import Workbook



# this loops to make many excel files automatically.

print("As long as the LORD liveth, I shall find private keys and addresses with good balances")
for j in range( 28, 40):
	wb = Workbook()

	headers = ['PRIVATE KEY', 'ADDRESS']
	ws = wb.active
	ws.append(headers)
	wbname = "pk" + str(j)+ ".xlsx"
	print ("Present file is " + wbname)
	print("triangulating....")
	
	for i in range(1,400000):
		priv = secrets.token_hex(32)
		private_key = "0x" + priv
		#print (priv)
		acct = Account.from_key(private_key)
		#print ("address :", acct.address)

		rows = [priv, acct.address]
		ws.append(rows)
	wb.save(wbname)
	#clear active worksheet so as not to repeat values in next loop
	ws = []
print("finito, God no go shame us!!")
#	with open ("priv.xlsx", "w") as text_file:
#		print (priv, file = text_file)
#		print (acct.address, file = text_file)
	