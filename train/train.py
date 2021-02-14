import pandas as pd
from sklearn.model_selection import train_test_split
# XGBoost Classification model
from xgboost import XGBClassifier
# Decision Tree model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Loading the data
data = pd.read_csv('./data/2021-2-13/urldata.csv')

# Dropping the Domain column
data = data.drop(['Domain'], axis = 1).copy()

# Plotting the data distribution
# uncomment to generate image (data.png)
# import matplotlib.pyplot as plt
# data.hist(bins = 50, figsize = (15,15))
# plt.show()

# Shuffling the rows to make them equally distributed for future training
data = data.sample(frac=1).reset_index(drop=True)

# Separating & assigning features and target columns to X & y
y = data['Label']
X = data.drop('Label', axis=1)

# Splitting the dataset into train and test sets: 80-20 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

# Creating holders to store the model performance results
ML_Model = []
acc_train = []
acc_test = []


# function to call for storing the results
def storeResults(model, a, b):
    ML_Model.append(model)
    acc_train.append(round(a, 3))
    acc_test.append(round(b, 3))


##################################################################################
# MODEL 1 XGBoost Classification model
xgb = XGBClassifier(learning_rate=0.4, max_depth=7)

# fit the model
xgb.fit(X_train, y_train)

# predicting the target value from the model for the samples
y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)

# computing the accuracy of the model performance
acc_train_xgb = accuracy_score(y_train, y_train_xgb)
acc_test_xgb = accuracy_score(y_test, y_test_xgb)

print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))
storeResults('XGBoost', acc_train_xgb, acc_test_xgb)


##################################################################################
# MODEL 2  Decision Tree Classifier
tree = DecisionTreeClassifier(max_depth=5)

# fit the model
tree.fit(X_train, y_train)

# predicting the target value from the model for the samples
y_test_tree = tree.predict(X_test)
y_train_tree = tree.predict(X_train)
# computing the accuracy of the model performance
acc_train_tree = accuracy_score(y_train, y_train_tree)
acc_test_tree = accuracy_score(y_test, y_test_tree)

print("Decision Tree: Accuracy on training Data: {:.3f}".format(acc_train_tree))
print("Decision Tree: Accuracy on test Data: {:.3f}".format(acc_test_tree))
storeResults('Decision Tree', acc_train_tree, acc_test_tree)
