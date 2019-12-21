#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:23:00 2019

@author: willdarden
"""
import pickle
from sklearn.neighbors import KNeighborsClassifier

config = {
        "k": 15
        }

def column(matrix, i):
    return [row[i] for row in matrix]

y_true = []
nImages = 0


##### DATA LOADING

with open( 'BlackJackAIDataLog.txt', 'r' ) as fp :
    raw = fp.read()
    
##SPLIT DATA STRINGS
raw = raw.split("\n")
raw = raw[:-1]
data = []
    
## GET DATA ROWS
for r in raw:
    row = r.split(',')
    y_true.append(1 if row[-1] == 'should-hit' else 0)
    row = row[:-1]
    for x in range(len(row)):
        row[x] = float(row[x])
    data.append(row)
formedData = data

##### MODEL CREATION
data = formedData
model = KNeighborsClassifier(config["k"]).fit(data, y_true)
#y_pred = model.labels_

pkl_filename = 'aiFile.mod'
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

#from sklearn.cluster import KMeans
#
#import pickle
#import numpy as np
#from sklearn.metrics import confusion_matrix
#from scipy.optimize import linear_sum_assignment
#import sys
#
#config = {
#        "k": 2
#        }
#
#def column(matrix, i):
#    return [row[i] for row in matrix]
#
#y_true = []
#nImages = 0
#
#
###### DATA LOADING
#
#with open( 'BlackJackAIDataLog.txt', 'r' ) as fp :
#    raw = fp.read()
#    
###SPLIT DATA STRINGS
#raw = raw.split("\n")
#raw = raw[:-1]
#data = []
#    
### GET DATA ROWS
#for r in raw:
#    row = r.split(',')
#    y_true.append(1 if row[-1] == 'should-hit' else 0)
#    row = row[:-1]
#    for x in range(len(row)):
#        row[x] = float(row[x])
#    data.append(row)
#formedData = data
#
###### MODEL CREATION
#data = formedData
#model = KMeans(n_clusters=config["k"], random_state=0).fit(data)
#y_pred = model.labels_
#
##### BUILD CONFUSION MATRIX
#confMat = confusion_matrix(y_true, y_pred)
#
##### MAXIMUM BIPARTITE GRAPH MATCHING
#trueCol = linear_sum_assignment(sys.maxsize - confMat)
#
#
##### REARANGE CONFUSION MATRIX USING BIPARTITE RESULT
#formattedConfMat = np.full((config["k"], config["k"]), 0)
#for i in range(config["k"]):
#    formattedConfMat[:,i] = confMat[:,trueCol[1][i]]
#
##### PRINT GRAPH AND COUNT TOTAL PREDICTIONS
#topLabels = ["  "]
#for i in range(config["k"]):
#    topLabels.append(str(i + 1))
#s = " "
#s = s.join(topLabels)
#print(s)
#totalCount = 0
#correctCount = 0
#for i in range(config["k"]):
#    correctCount = correctCount + formattedConfMat[i,i]
#    totalCount = totalCount + np.sum(formattedConfMat[i])
#    print(i + 1, formattedConfMat[i].tolist())
#

#accuracy = correctCount / totalCount
#print("Total count: %d, Correct Count: %d, Accuracy: %f" % (totalCount, correctCount, accuracy))
#
#pkl_filename = 'aiFile.mod'
#with open(pkl_filename, 'wb') as file:
#    pickle.dump(model, file)




