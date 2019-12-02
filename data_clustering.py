# -*- coding: utf-8 -*-
"""
Integrates the K-Means Algorithm of Data clustering

@author: Ujjaini
"""
import pandas as pd
from pandas import DataFrame
from oct2py import Oct2Py
oc = Oct2Py()

def find_closest_centroids(X, centroids):
    K = oc.size(centroids, 1)
    idx = oc.zeros(oc.size(X, 1), 1)
    m = oc.size(X,1)
    for i in range(m):
        min_dist = 1000000000
        for j in range(K):
            vector = X[i,:] - centroids[j,:]
            dist = oc.sum(vector^2)
            if dist < min_dist:
                idx[i] = j
                min_dist = dist
    return idx

def compute_centroids(X, idx, K):
    [m, n] = oc.size(X)
    centroids = oc.zeros(K, n)
    ck = oc.zeros(K, 1)
    for i in range(K):
        for j in range(m):
            if(idx[j, 1] == i):
                centroids[i,:] = centroids[i,:] + X[j,:]
                ck[i] = ck[i] + 1
        centroids[i,:] = centroids[i,:]/ck[i]
    return centroids

def init_centroids(X, K):
    centroids = oc.zeros(K, oc.size(X, 2))
    randidx = oc.randperm(oc.size(X, 1))
    centroids = X[randidx[0:K], :]
    return centroids



centroids = oc.zeros(2, 3)
print(centroids)
print(find_closest_centroids(centroids, 0))
print(centroids[0,:])


    

