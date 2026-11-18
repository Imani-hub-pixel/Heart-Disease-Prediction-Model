from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import pickle
import os
application=Flask(__name__)
app=application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "Notebook/heartdiseasepred.pkl"), "rb") as f:
    model = pickle.load(f)


## model=pickle.load(open("Notebook/heartdiseasepred.pkl",'rb'))

features_fields = {
    'gender': ("Gender", "select", {"0": "female", "1": "male"}),
    'age': ("Age", "Number", None),
    'education': ("Education Level(1-4)", "select", {"1": "1", "2": "2", "3": "3", "4": "4"}),
    'currentSmoker': ("Current Smoker", "select", {"0": "No", "1": "Yes"}),
    'cigsPerDay': ("Number of Cigarettes Per Day", "Number", None),
    'BPMeds': ("Taking Blood Pressure Medicine", "select", {"0": "No", "1": "Yes"}),
    'prevalentStroke': ("History of stroke", "select", {"0": "No", "1": "Yes"}),
    'prevalentHyp': ("Hypertensive", "select", {"0": "No", "1": "Yes"}),
    'diabetes': ("Daibetic", "select", {"0": "No", "1": "Yes"}),
    'totChol': ("Total Cholestrol", "Number", None),
    'sysBP': ("Systolic Blood Pressure", "Number", None),
    'diaBP': ("Diastolic Blood Pressure", "Number", None),
    'BMI': ("Body Max Index", "Number", None),
    'heartRate': ("Heart Rate", "Number", None),
    'glucose': ("Glucose", "Number", None)
}
features=list(features_fields)
required_features=['gender','age','sysBP','diaBP']


def predict_from_dict(data):
    row = {}
    for f in features:
        v = data.get(f)
        if v is None or str(v).strip() == "":
            if f in required_features:
                raise ValueError(f"'{f}' is required")
            row[f] = np.nan
        else:
            row[f] = float(v)
    prob = model.predict_proba(pd.DataFrame([row]))[0, 1]
    return int(prob >= 0.5), float(prob)

@app.route("/")
def home():
    return render_template('index.html',fields=features_fields,required=required_features)

@app.route("/predict",methods=['POST'])
def predict():
    try:
        label, prob = predict_from_dict(request.form)
    except ValueError as e:
        return render_template("index.html", fields=features_fields, required=required_features,
                               error=str(e), form=request.form)
    return render_template("index.html", fields=features_fields, required=required_features,
                           label=label, prob=round(prob * 100, 1), form=request.form)

@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error="Send a JSON body"), 400
    try:
        label, prob = predict_from_dict(data)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    return jsonify(prediction=label, probability=prob)

if __name__ == "__main__":
    app.run(debug=True)