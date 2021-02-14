import pickle
import pandas as pd
from url_parser import featureExtraction, feature_names

loaded_model = pickle.load(open("models/XGBoostClassifier.pickle.dat", "rb"))

feature_list = [featureExtraction("https://paypal.com.us.home.login.page.loginchecks.xyz/")]
print(feature_list)

pd.set_option('display.max_columns', None)
df = pd.DataFrame(feature_list, columns=feature_names)
print(df)

print(loaded_model.predict(df))
