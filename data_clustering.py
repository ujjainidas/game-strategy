# -*- coding: utf-8 -*-
"""
Integrates the K-Means Algorithm of Data clustering

@author: Ujjaini
"""
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from oct2py import Oct2Py
oc = Oct2Py()

def find_closest_centroids(X, centroids):
    print("A")
    K = oc.size(centroids, 1)
    print("B")
    idx = oc.zeros(oc.size(X, 1), 1)
    print("C")
    m = oc.size(X,1)
    print("D")
    for i in range(int(m)):
        min_dist = 1000000000
        for j in range(int(K)):
            vector = X.iloc[i,:] - centroids.iloc[j,:]
            dist = oc.sum(vector^2)
            if dist < min_dist:
                idx[i] = j
                min_dist = dist
            print("**********")
            print(str(i) + "    " + str(j))
            print(i*j)
    return idx

def compute_centroids(X, idx, K):
    print(oc.size(X))
    m = oc.size(X,1)
    n = oc.size(X,2)
    centroids = oc.zeros(K, n)
    ck = oc.zeros(K, 1)
    for i in range(K):
        for j in range(int(m)):
            if(idx[j, 1] == i):
                centroids[i,:] = centroids[i,:] + X[j,:]
                ck[i] = ck[i] + 1
        centroids[i,:] = centroids[i,:]/ck[i]
    return centroids

def init_centroids(X, K):
    centroids = oc.zeros(K, oc.size(X, 2))
    randidx = oc.randperm(oc.size(X, 1))
    print(centroids)
    print(len(randidx[0]))
    centroids = X.iloc[randidx[0][0:K], :]
    return centroids

data = pd.read_csv("2019data.csv")
data = data.drop("delete", axis = 1)
data = data.drop("dq", axis = 1)
data = data.drop("matches_played", axis = 1)
data = data.drop("rank", axis = 1)
data = data.drop("team_key", axis = 1)
data = data.drop("losses", axis = 1)
data = data.drop("wins", axis = 1)
data = data.drop("ties", axis = 1)
data = data.drop("ranking_score", axis = 1)
data = data.drop("ranking_points", axis = 1)
data = data.drop("qual_average", axis = 1)
data = data.iloc[0:1000,:]
print(data)

centroids = init_centroids(data, 4)
print(centroids)
for i in range(10):
    print(i)
    idx = find_closest_centroids(data, centroids)
    print(idx)
    centroids = compute_centroids(data, idx, 4)
    print(centroids)




    

