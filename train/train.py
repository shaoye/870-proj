import pandas as pd
from sklearn.model_selection import train_test_split
# XGBoost Classification model
from xgboost import XGBClassifier
# Decision Tree model
from sklearn.tree import DecisionTreeClassifier
# SVM model
from sklearn.svm import SVC
# Multilayer Perceptions model
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
import pickle
import numpy as np

# Loading the data
data = pd.read_csv('./data/2021-03-15/urldata.csv')

# Dropping the Domain column
data = data.drop(['Domain'], axis=1).copy()

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


# function for storing the results
def store_results(model, a, b):
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
store_results('XGBoost', acc_train_xgb, acc_test_xgb)
# saving the model for future use
pickle.dump(xgb, open("../models/XGBoostClassifier.pickle.dat", "wb"))

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
store_results('Decision Tree', acc_train_tree, acc_test_tree)
# saving the model for future use
pickle.dump(tree, open("../models/DecisionTreeClassifier.pickle.dat", "wb"))

##################################################################################
# MODEL 3  SVM (Support vector machine) model
svm = SVC(kernel='linear', C=1.0, random_state=12, probability=True)
# fit the model
svm.fit(X_train, y_train)
# predicting the target value from the model for the samples
y_test_svm = svm.predict(X_test)
y_train_svm = svm.predict(X_train)
# computing the accuracy of the model performance
acc_train_svm = accuracy_score(y_train, y_train_svm)
acc_test_svm = accuracy_score(y_test, y_test_svm)

print("SVM: Accuracy on training Data: {:.3f}".format(acc_train_svm))
print("SVM : Accuracy on test Data: {:.3f}".format(acc_test_svm))
store_results('SVM', acc_train_svm, acc_test_svm)
# saving the model for future use
pickle.dump(svm, open("../models/SVMClassifier.pickle.dat", "wb"))

##################################################################################
# MODEL 4  MLP (Multilayer Perceptions) Deep Learning model
mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100, 100, 100]))
mlp.fit(X_train, y_train)
y_test_mlp = mlp.predict(X_test)
y_train_mlp = mlp.predict(X_train)

acc_train_mlp = accuracy_score(y_train, y_train_mlp)
acc_test_mlp = accuracy_score(y_test, y_test_mlp)

print("Multilayer Perceptions: Accuracy on training Data: {:.3f}".format(acc_train_mlp))
print("Multilayer Perceptions: Accuracy on test Data: {:.3f}".format(acc_test_mlp))
store_results('Multilayer Perceptions', acc_train_mlp, acc_test_mlp)
# saving the model for future use
pickle.dump(mlp, open("../models/MLPClassifier.pickle.dat", "wb"))

##################################################################################
# Comparision of Models
results = pd.DataFrame({'ML Model': ML_Model,
                        'Train Accuracy': acc_train,
                        'Test Accuracy': acc_test})
print(results.sort_values(by=['Test Accuracy', 'Train Accuracy'], ascending=False))
