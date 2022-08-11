from eth_account import Account
from openpyxl import Workbook
wb = Workbook()
headers = ['PRIVATE KEY', 'ADDRESS']
ws = wb.active
#ws.append(headers)



private_key ="ffe8b2eabec7247b085c243d6c529501a166d47e484cc1454d60c930c6bc985"
i = int(private_key, 16)
i += 500001
print (hex(i))
private_key = hex(i)
row = [private_key]
ws.append(row)
wb.save("lastpk.xlsx")