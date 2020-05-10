"""
linear-regression
Create multiple models and saving ones that generate the best scores.
 https://techwithtim.net/tutorials/machine-learning-python/saving-models/
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")
# Since our data is separated by semicolons we need to do sep=";"
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# print(data.head())

'''
#Separating Our Data
  G1 ,G2 - first second period grade  
  G3 - final grade  
label is attribute we are trying to predict (G3 ). 
features is the  attributes that will determine our label(G1, G2 ).  

we will use numpy to create two arrays.
 One that contains all of our features (G1, G2 ) and one that contains 
 our labels (G3 ).
'''
predict = "G3"

X = np.array(data.drop([predict], 1))  # Features: All columns without G3
y = np.array(data[predict])  # Labels: only G3 column
'''
Split our data into testing and training data.
 90% of data to train and the other 10% to test. 
'''
x_train, x_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# Implementing the Algorithm
linear = linear_model.LinearRegression()  # defining the model

pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

# Now we can use linear to predict grades like before

# linear is the name of the model we created in line 48
#
