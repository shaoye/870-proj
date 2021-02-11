import pickle

loaded_model = pickle.load(open("models/XGBoostClassifier.pickle.dat", "rb"))

# loaded_model.predict_prob()