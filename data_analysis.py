# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:37:13 2019

@author: Ujjaini Das
"""
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

team_data2 = pd.read_csv("2019data.csv")

descriptive_stats = team_data.describe()
#descriptive_stats.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\descriptive_stats.csv')

def cleanData(data_set):
    cleaned_data = data_set
    cleaned_data.drop('team_key',1)
    cleaned_data.drop('qual_average',1)
    for c in cleaned_data.columns:
        cleaned_data[c] = cleaned_data[c].fillna(0)
    return cleaned_data

team_data_cleaned = cleanData(team_data2)

team_target_name = "rank"
team_target = team_data_cleaned[team_target_name]
fig = plt.figure(figsize = (10,10))

#plt.scatter(team_data['hab'], team_data[team_target_name])
#plt.scatter(team_data['cargo'], team_data[team_target_name])
#plt.scatter(team_data['hatch'], team_data[team_target_name])
#plt.scatter(team_data['sandstorm_bonus'], team_data[team_target_name])
#plt.scatter(team_data['ranking_points'], team_data[team_target_name])
#plt.scatter(team_data['ranking_score'], team_data[team_target_name])
#plt.scatter(team_data['losses'], team_data[team_target_name])
#plt.scatter(team_data['wins'], team_data[team_target_name])
#plt.scatter(team_data['ties'], team_data[team_target_name])
#plt.scatter(team_data['dq'], team_data[team_target_name])
#plt.show()

corrmat = team_data_cleaned.corr()
f = sns.heatmap(corrmat, vmax=.8, square=True, annot=True, cbar=False)



