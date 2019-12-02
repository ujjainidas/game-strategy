
"""This file extracts data using the tbapy library from The Blue Alliance API

@author Ujjaini Das
"""

import tbapy
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
from oct2py import Oct2Py
oc = Oct2Py()

tba = tbapy.TBA("MtsQ8UR2BsMQ03giTxFXqNbP61OyHF1Sy9VNNKbK8UjtBfr8NQfYF7Gbs7XrDkoA")

event_list = tba.events('2019', keys = True)

rankings = tba.event_rankings('2019txdel')
df = pd.DataFrame(rankings['rankings'])
event_list.remove('2019txdel')

for i in event_list:
    rankings = tba.event_rankings(i)
    df = pd.concat([df, pd.DataFrame(rankings['rankings'])], axis = 0)
   
print(df)

losses = []
wins = []
ties = []
ranking_score = []
cargo = []
hatch = []
hab = []
sandstorm_bonus = []
ranking_points = []

for index, row in df.iterrows():
    losses.append(row['record']['losses'])
    wins.append(row['record']['wins'])
    ties.append(row['record']['ties'])
    ranking_score.append(row['sort_orders'][0])
    cargo.append(row['sort_orders'][1])
    hatch.append(row['sort_orders'][2])
    hab.append(row['sort_orders'][3])
    sandstorm_bonus.append(row['sort_orders'][4])
    ranking_points.append(row['extra_stats'][0])
 
df['losses'] = np.asarray(losses)
df['wins'] = np.asarray(wins)
df['ties'] = np.asarray(ties)
df['ranking_score'] = np.asarray(ranking_score)
df['cargo'] = np.asarray(cargo)
df['hatch'] = np.asarray(hatch)
df['hab'] = np.asarray(hab)
df['sandstorm_bonus'] = np.asarray(sandstorm_bonus)
df['ranking_points'] = np.asarray(ranking_points)

df = df.drop('record', axis = 1)
df = df.drop('sort_orders', axis = 1)
df = df.drop('extra_stats', axis = 1)


    


#df.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\2019data.csv')

