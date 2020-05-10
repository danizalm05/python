"""
linear-regression1
 predict grade G3 from this 5 variables:
                G1, G2 ,  "studytime", "failures", "absences"

https://techwithtim.net/tutorials/machine-learning-python/linear-regression/
https://techwithtim.net/tutorials/machine-learning-python/linear-regression-2/
Data Set Description: https://archive.ics.uci.edu/ml/datasets/Student+Performance
Data Set:  https://archive.ics.uci.edu/ml/machine-learning-databases/00320/
"""
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
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
# train and score our model using the arrays we created in the previous tutorial.
linear.fit(x_train, y_train)  # Train  the model
acc = linear.score(x_test, y_test)  # acc stands for accuracy
#  For this specific data set a score of above 80% is fairly good.
print('accuracy:\n', acc)
print('Coefficient: \n', linear.coef_)  # These are each slope value. Since we have
                                        # 5 variables we will  have 5 Coefficients
print('Intercept: \n', linear.intercept_)  # This is the intercept
#  Predicting on Specific Students
#  print  test  data,   actual final gradeand predicted grade.
predictions = linear.predict(x_test)  # Gets a list of all predictions
print("prediction         [G1  G2 ...... ]  Real final result(test)")
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

#Save our model( we will )write to a new file using pickle.dump())

fn = "studentgrades.pickle"
with open(fn, "wb") as f:
    pickle.dump(linear, f)
print("Model saved to file ", fn)