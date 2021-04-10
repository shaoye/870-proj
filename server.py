from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import pandas as pd
from url_parser import featureExtraction, feature_names

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# load 4 pre-trained models
xgboost_model = pickle.load(open("models/XGBoostClassifier.pickle.dat", "rb"))
decision_tree_model = pickle.load(open("models/DecisionTreeClassifier.pickle.dat", "rb"))
svm_model = pickle.load(open("models/SVMClassifier.pickle.dat", "rb"))
mlp_model = pickle.load(open("models/MLPClassifier.pickle.dat", "rb"))


@app.route('/check', methods=['POST'])
def check_phishing():
    data = request.get_json()
    print(data)
    test_url = data['url']
    if test_url is None:
        return '', 400

    feature_list = [featureExtraction(test_url)]
    df = pd.DataFrame(feature_list, columns=feature_names)
    prob_1 = xgboost_model.predict_proba(df)
    prob_2 = decision_tree_model.predict_proba(df)
    prob_3 = svm_model.predict_proba(df)
    prob_4 = mlp_model.predict_proba(df)

    result_1 = xgboost_model.predict(df)
    result_2 = decision_tree_model.predict(df)
    result_3 = svm_model.predict(df)
    result_4 = mlp_model.predict(df)

    results = pd.DataFrame({'ML Model': ["XGBoost", "Decision Tree", "SVM", "Multilayer Perceptions"],
                            'Probability': [prob_1, prob_2, prob_3, prob_4],
                            'Result': [result_1, result_2, result_3, result_4]})

    return jsonify(results.to_json(orient='records')), 200


if __name__ == '__main__':
    app.run(debug=True)
