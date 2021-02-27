import re
import sys
import pandas as pd
#from encapsulate import encapsulate_all
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn import svm
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.decomposition import PCA
#import braces_similarity as bs, comment_similarity as cs
#import WPSR as ws, karp as ss
#import total_no_of_unused as tnu
import math
import pygments.token
import pygments.lexers
import subprocess
import numpy as np
import os



import pickle

# read from csv files and combine them
df1 = pd.read_csv('C:/Users/mitesh pandey/Downloads/data_2016_200.csv')
df2 = pd.read_csv('C:/Users/mitesh pandey/Downloads/data_2017_200.csv')
dataframe = pd.concat([df1, df2])


X = dataframe.iloc[:, 3:]
dataframe.plag_results = pd.Categorical(dataframe.plag_results)
Y = dataframe.plag_results.cat.codes

#print(Y.head())


# split data into train and test sets
#seed = 7
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, stratify=Y)
# fit model no training data
model = XGBClassifier()
# model = svm.SVC()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
f1_Score = f1_score(y_test, predictions)
print("F1 score without cross validation: %.2f%%" % (f1_Score * 100.0))
accuracy_Score = accuracy_score(y_test, predictions)
print("Accuracy without cross validation: %.2f%%" % (accuracy_Score * 100.0))

pickle.dump(model, open(os.getcwd()+'/xg.dat', "wb"))