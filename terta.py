from eth_account import Account
import csv

priv = "aeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeae"

acct = Account.from_key("0x" +priv)
address = acct.address
print(address)

number = 100000000000000000000000000000000000000000000000000001234567891223000000780

numhex = hex(number)
print(numhex)
print( "Length " +str(len(numhex)))
print(len(str(number)))

bignum = (2 **256) - 1
print(bignum)
print(hex(bignum))

print("Eth-account starts here")


for i in range(1,1000000):
	wallet = Account.create('Xavier')
	print(wallet.key.hex())
	print("Address is: " + wallet.address)
	row = [wallet.key.hex(), wallet.address.lower()]
	with open ("pk8.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerow(row)