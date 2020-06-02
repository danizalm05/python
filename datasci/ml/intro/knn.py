"""
https://techwithtim.net/tutorials/machine-learning-python/k-nearest-neighbors-1/
 KNN = K-Nearest Neighbors.
  KNN   attempts to classify data into certain categories.
 We will be using this algorithm to classify cars in 4 categories based upon certain features.
"""
"""
Class Values:
   unacc, acc, good, vgood
Attributes:

buying: vhigh, high, med, low.
maint: vhigh, high, med, low.
doors: 2, 3, 4, 5more.
persons: 2, 4, more.
lug_boot: small, med, big.
safety: low, med, high. 
"""
from sklearn import preprocessing
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#Loading Data car.data

data = pd.read_csv("car.data")
print(data.head())  # To check if our data is loaded correctly
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))# [3 3 3 ... 1 1 1].
maint = le.fit_transform(list(data["maint"]))#[3 3 3 ... 1 1 1]
door = le.fit_transform(list(data["door"]))#[0 0 0 ... 3 3 3]
persons = le.fit_transform(list(data["persons"]))#[0 0 0 ... 2 2 2]
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))#[1 2 0 ... 1 2 0]
cls = le.fit_transform(list(data["class"]))#[2 2 2 ... 2 1 3]

print(cls)
# Recombine our data into a feature list and a label list.
# We can use the zip() function to makes things easier.

X = list(zip(buying, maint, door, persons, lug_boot, safety))  # features
y = list(cls)  # labels
#print(X)
#Split our data into training and testing data using the same process seen previously.

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

#https://techwithtim.net/tutorials/machine-learning-python/k-nearest-neighbors-3/

##Training a KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=9)
model.fit(x_train, y_train)# train our model
acc = model.score(x_test, y_test)# score our model
print("Accurecy = ",acc)
#Testing Our Model 

predicted = model.predict(x_test)
# Create a names list so that we can convert our integer predictions into 
# their string representation 
names = ["unacc", "acc", "good", "vgood"]
#predicted
print ("Nuber of items = ",len(predicted))
for x in range(len(predicted)):
 print("Predicted = ", names[predicted[x]], "    Data: ", x_test[x], "Actual: ", names[y_test[x]])
 
 #Looking at Neighbors
 redicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    # See the neighbors of each point in our testing data
    n = model.kneighbors([x_test[x]], 9, True)
    #This will return to us:
    #   1: an array with the index in our data of each neighbor. 
    #   2: If distance=True then it will also return the distance to each 
    #        neighbor from our data point.
    #x_test[x ] = one  line in data array
    print
    print("[",x,"]")
    print("    N: ", n)
    print("-------------------------")