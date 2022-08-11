import numpy as np
import secrets
from eth_account import Account
import csv

for i in range(1, 10):
	priv = secrets.token_hex(32)
	bass = np.array([priv, Account.from_key("0x"+priv).address.lower()])
	print(bass)
	
	#with open ("chunk1.csv", 'r', ) as f:
	#	alto = list(csv.reader(f, delimiter = ','))
#		altonp = np.array(alto)
#	print(altonp)
	
#	tenor = np.intersect1d(bass, altonp)
#	print(tenor)