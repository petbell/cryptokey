import numpy as np
from eth_account import Account
import secrets
from openpyxl import Workbook

arr = np.array ([])
#for i in range(1,400000):
priv = secrets.token_hex(32)
private_key = "0x" + priv
		#print (priv)
acct = Account.from_key(private_key)
		#print ("address :", acct.address)

rows = [priv, acct.address]
arr.append(rows)