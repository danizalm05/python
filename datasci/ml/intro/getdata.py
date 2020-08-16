"""
linear-regression1
 predict grade G3 from this 5 variables:
                G1, G2 ,  "studytime", "failures", "absences"

https://techwithtim.net/tutorials/machine-learning-python/linear-regression/
https://techwithtim.net/tutorials/machine-learning-python/linear-regression-2/
https://techwithtim.net/tutorials/machine-learning-python/saving-models/
Data Set Description: https://archive.ics.uci.edu/ml/datasets/Student+Performance

Data Set:  https://archive.ics.uci.edu/ml/machine-learning-databases/00320/
"""
import torch
import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle


'''
#Separating Our Data
  G1 ,G2 - first second period grade ,"absences","failures", "studytime" 
  G3 - final grade  
label is attribute we are trying to predict (G3 ). 
features is the  attributes that will determine our label(G1, G2.... ).  

we will use numpy to create two arrays.
 One that contains all of our features (G1, G2 ) and one that contains 
our labels (G3 ).
'''
style.use("ggplot")
data = pd.read_csv("student-mat.csv", sep=";")
predict = "G3"
data = data[["G1", "G2", "absences","failures", "studytime","G3"]]
data = shuffle(data) # Optional - shuffle the data

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = \
                       sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# TRAIN MODEL MULTIPLE TIMES FOR BEST SCORE
best = 0
for i in range(20):
    x_train, x_test, y_train, y_test = \
            sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy [", i, "]: " + str(acc))

    if acc > best:
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)

# LOAD MODEL
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)


print("----Best acc = ", best , " ---------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")
# At this point liner varible
predicted = linear.predict(x_test)
for x in range(len(predicted)):
    print(predicted[x], x_test[x], y_test[x])


# Drawing and plotting model
plot = "studytime"# "failures"
plt.scatter(data[plot], data["G3"])
plt.legend(loc=4)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()