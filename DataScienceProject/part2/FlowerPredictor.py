
import pandas
import matplotlib.pyplot as plt
import sklearn

dataframe = pandas.read_csv('https://modcom.co.ke/data/datasets/iris.csv')
print(dataframe)

# Step 1: split data into features and outcome
array = dataframe.values
# print(array)
X = array[:, 0:4] # always a -1 , upto 3: features
Y = array[:, 4]  # 4th counted here: outcome

# Step 2: split data into training set and test set.
# 70% for training , 30% for test set
from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,
                                                                test_size=0.30,
                                                                random_state=2)


# Step 3: Create algorithms/model and expose the X_train, Y_train = 70% of data
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

model = DecisionTreeClassifier()
model.fit(X_train, Y_train) # we hide x_test, y_test from the model
print('Training....') # above is the learning part

#Step 4: Test your model
# Ask the model now to predict x_test, hide y_test -  outcomes
predictions = model.predict(X_test)
print(Y_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,predictions))

from sklearn.metrics import classification_report
print(classification_report(Y_test,predictions))









