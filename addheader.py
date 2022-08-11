import pandas as pd
import csv

headerList = ['rank', 'address','c', 'name', ' tag', 'balance', 'percentage', 'txn count', 'b', 'k']
premine = pd.read_csv("polygon_accounts.csv")
premine.to_csv('pk6.csv', header= headerList, index= 'False')

postmine = pd.read_csv("pk6.csv")
print(postmine['address'].head(5))