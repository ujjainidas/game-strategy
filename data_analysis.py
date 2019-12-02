# -*- coding: utf-8 -*-
"""
This file plots data sets in relation to the prediction value. 

@author: Ujjaini Das
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

team_data = pd.read_csv("2019data.csv")
team_data = team_data.drop('delete', axis=1)
team_data = team_data.drop('team_key', axis=1)
team_data = team_data.drop('qual_average', axis=1)

descriptive_stats = team_data.describe()
#descriptive_stats.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\descriptive_stats.csv')

print(team_data)

#team_data.to_csv(r'C:\Users\thisi\Desktop\Machine Learning\game-strategy\team_data_cleaned.csv')



team_target_name = "rank"
team_target = team_data[team_target_name]
fig = plt.figure(figsize = (10,10))

#for(i, column) in enumerate(list(team_data.columns)):
#    if(column == team_target_name):
#        continue;
#    plt.subplot(5,3,i)
#    plt.scatter(team_data[column], team_data[team_target_name])
#    plt.xlabel(column)
#    plt.ylabel(team_target_name)
#
#plt.show()

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
#
#corrmat = team_data.corr()
#f = sns.heatmap(corrmat, vmax=.8, square=True, annot=True, cbar=False)

team_data_copy = team_data.copy()
features = team_data_copy.drop(["rank"], 1)
predict = team_data_copy[team_target_name]


sc = StandardScaler()

features = pd.DataFrame(sc.fit_transform(features.values), index = features.index, columns = features.columns)

train_X, test_X, train_Y, test_Y = train_test_split(features, predict, test_size = 0.08, random_state = 150)

linReg = LinearRegression()
model = linReg.fit(train_X, train_Y)

print(model.coef_)


prediction = linReg.predict(test_X)

print(prediction)

print(linReg.score(test_X, test_Y))


