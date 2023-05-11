# import necessary libraries
import os
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Model Setup
#################################################

from joblib import load
model_path = os.environ.get('MODEL_PATH', '') or "model.joblib"
print("Loading model...")
model = load(model_path)

#################################################
# Web User Interface - Front End
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

#################################################
# API - Back End
#################################################


@app.route("/api/predict", methods=["POST"])
def predict():
    labels = ['Resuscitation: 2mins', 'Emergency: 10mins', 'Urgent: 30min', 'Semi-Urgent: 60mins', 'Non-Urgent: 120mins']
    sex = int(request.form["Sex"])
    age = int(request.form["Age"])
    arrival_mode = int(request.form["Arrival mode"])
    injury = int(request.form["Injury"])
    mental = int(request.form["Mental"])
    pain = int(request.form["Pain"])
    nrs_pain = int(request.form["NRS_pain"])
    sbp = float(request.form["SBP"])
    dbp = float(request.form["DBP"])
    hr = float(request.form["HR"])
    rr = float(request.form["RR"])
    bt = float(request.form["BT"])
    saturation = float(request.form["Saturation"])

    index = model.predict(X)[0]

    return jsonify(f"Predicted Triage Category: {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
