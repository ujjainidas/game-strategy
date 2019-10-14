
"""This file extracts data using the tbapy library from the Blue Alliance API

@author Ujjaini Das
"""

import tbapy
from pandas import DataFrame
from oct2py import Oct2Py
oc = Oct2Py()

print(oc.abs(-1))

tba = tbapy.TBA("MtsQ8UR2BsMQ03giTxFXqNbP61OyHF1Sy9VNNKbK8UjtBfr8NQfYF7Gbs7XrDkoA")

event_list = tba.events("2019", keys = True)

teams = tba.teams()

team_254 = tba.team_robots(254)

awards = tba.event_awards('2019txdel')

print(event_list)
print("\n\n")

for x in team_254:
    print("\n\n")
    print(x)
    
print ("\n\n")


for y in awards:
    print("\n")
    print(y)
    
df = DataFrame(awards, columns = ['event_key', 'name', 'recipient_list', 'year'])

export_csv = df.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\export_dataframe.csv', 
                       index = None, header = True)

df2 = new DataFrame(team_254, columnns = ['key', 'robot_name', 'year'])

team_254_csv = df2.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\team_254.csv', 
                       index = None, header = True)

print(df)

#for x in teams:
    #print("\n\n")
    #print(x)
