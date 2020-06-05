"""
https://techwithtim.net/tutorials/machine-learning-python/svm-1/
 Support Vector Machines (SVM)


SVM's are  similar to   K Nearest Neighbors. 
used to classify data that does not have a linear correspondence.

Scikit-learn is  machine learning library  
 It features various classification, regression and 
 clustering algorithms  

 
"""
import sklearn
from sklearn import svm
from sklearn import datasets
# scikit-learn comes with a few small standard datasets that do not
# require to download any file from some external website.
cancer = datasets.load_breast_cancer()
print("\n\nFeatures: ", cancer.feature_names)#list of features in the data set
print("\n\nLabels: ", cancer.target_names)#list of label



x = cancer.data  # All of the features
y = cancer.target  # All of the labels

#Splitting Data

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
#print the first few instances
print('\n\nx_train\n',x_train[:5],'\n\ny_train \n ', y_train[:5])
#https://techwithtim.net/tutorials/machine-learning-python/svm-2/#What a SVM Does?
"""
What a SVM Does?  https://techwithtim.net/tutorials/machine-learning-python/svm-2/

SVM is a tool for classifying complicated data with a high degree of dimensions(features).
K-Nearest Neighbors does not perform well on high-dimensional data.

"""
#Implementing a SVM

#https://techwithtim.net/tutorials/machine-learning-python/svm-p-3-implementation/
from sklearn import svm
 
clf = svm.SVC() #create a new model
clf.fit(x_train, y_train)

from sklearn import metrics
 
y_pred = clf.predict(x_test) # Predict values for our test data
acc = metrics.accuracy_score(y_test, y_pred) # Test them against our correct values
print("\n\n SVM naccuracy =  ",acc,"\n\n")
"""
Our accuracy is close to 60% and that is horrible! 
 Looks like we need to add something else.
 
  Adding a Kernel

The reason we received such a low accuracy score was we forgot to add a kernel! We need to specify which kernel we should use to increase our accuracy.

Kernel Options:

    linear
    poly
    rbf
    sigmoid
    precomputed

We will use linear for this data-set.

 """
clf = svm.SVC(kernel="linear") 
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test) # Predict values for our test data

acc = metrics.accuracy_score(y_test, y_pred) # Test them against our correct values
print("\n\nSVM + Kernel naccuracy =  ",acc,"")

"""
Comparing to KNearestNeighbors

If we want to see how this algorithm runs in comparison to KNN we can run the KNN classifier on this data-set and compare our accuracy values.

"""
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=11)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test) # Predict values for our test data

acc = metrics.accuracy_score(y_test, y_pred) # Test them against our correct values
print("knn accuracy =  ",acc,"\n\n")