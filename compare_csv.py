import pandas as pd
import csv
import numpy as np

olddf = pd.read_csv('ether_addresses.csv')
#print(olddf.head(5))
oldnp = np.array(olddf['address'])
print(oldnp)

newdf = pd.read_csv('ether_addresses1.csv')
#print(newdf.head(5))
newnp = np.array(newdf['address'])
print(newnp)

#match = np.intersect1d( oldnp, newnp)
#print(match.size)