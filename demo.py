# For any given url, use this file to get machine learning results form 4 pre-trained models.
import pickle
import pandas as pd
from url_parser import featureExtraction, feature_names

# URL to check
test_url = "https://paypal.com.us.home.login.page.loginchecks.xyz/"
# test_url = "https://evernote.com/register?upgrade=premium&itemCode=premium-1year&offer=www_pricing_CTA"

# load 4 pre-trained models
xgboost_model = pickle.load(open("models/XGBoostClassifier.pickle.dat", "rb"))
decision_tree_model = pickle.load(open("models/DecisionTreeClassifier.pickle.dat", "rb"))
svm_model = pickle.load(open("models/SVMClassifier.pickle.dat", "rb"))
mlp_model = pickle.load(open("models/MLPClassifier.pickle.dat", "rb"))

feature_list = [featureExtraction(test_url)]
df = pd.DataFrame(feature_list, columns=feature_names)
result_1 = xgboost_model.predict_proba(df)
result_2 = decision_tree_model.predict_proba(df)
result_3 = svm_model.predict_proba(df)
result_4 = mlp_model.predict_proba(df)

results = pd.DataFrame({'ML Model': ["XGBoost", "Decision Tree", "SVM", "Multilayer Perceptions"],
                        'Result': [result_1, result_2, result_3, result_4]})
print("#########################################################################")
print("Result [0]: Probability of Benign URL")
print("Result [1]: Probability of Malicious URL for phishing ")
print("#########################################################################")
print(results)
