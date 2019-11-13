# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:29:38 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as graph
#import tensorflow as tf

#from sklearn import datasets
#from sklearn import metrics
#from sklearn.svm import SVC

sharefile = pd.read_csv('Sharefile.txt', sep=',')
arr= np.array(sharefile)
#sharefile = pd.read_csv('Sharefile.txt',sep =',')
#Output = sharefile.head(5)
#graph.plot(Output,Output,label='linear')
#print (Output)
#DataShape = sharefile.columns
#print(DataShape)
YearHighSort = sharefile.sort_values(['Growth(%)','PriceDiff'], ascending = False)
print(YearHighSort)
f = open("SortedSharefile.txt", "w")
f.write(str(YearHighSort))
f.close()
print('--------------------------------------------')
print(arr)
print(arr[2,2])
#print(arr.sum(axis=1))

#ds = datasets.load_iris()
#model = SVC()
#model.fit(ds.data,ds.target)
#print(model)
#print("/n")

#expected = ds.target
#predicted = model.predict(ds.data)
#print(metrics.classification_report (expected,predicted))