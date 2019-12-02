# -*- coding: utf-8 -*-

import tbapy
import pandas as pd
tba = tbapy.TBA("MtsQ8UR2BsMQ03giTxFXqNbP61OyHF1Sy9VNNKbK8UjtBfr8NQfYF7Gbs7XrDkoA")

event_list = tba.events('2019', keys = True)

delrio = tba.event_alliances('2019txdel')
print(delrio)

for i in delrio:
    if(len(i['picks']) is 3):
            pick_one = i['picks'][0]
            pick_two = i['picks'][1]
            pick_three = i['picks'][2]
for i in event_list:
    alliances = tba.event_alliances(i)
    rankings = tba.event_rankings(i)
    for j in alliances: 
        if(len(j['picks']) is 3):
            pick_one = j['picks'][0]
            pick_two = j['picks'][1]
            pick_three = j['picks'][2]
        data = [[1, pick_one], [2, pick_two], [3, pick_three]]
        df = df.append(pd.DataFrame(data, columns = ['Pick', 'Team']))


print(df)
        
        

