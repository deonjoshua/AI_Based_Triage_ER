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


@app.route('/api/predict', methods=['POST'])
def predict():
    labels = ['Resuscitation: 2mins', 'Emergency: 10mins', 'Urgent: 30min', 'Semi-Urgent: 60mins', 'Non-Urgent: 120mins']
    # Capture the inputs from the form
    input_data = {
        'Sex': [int(request.form['Sex'])],
        'Age': [int(request.form['Age'])],
        'Arrival mode': [int(request.form['Arrival mode'])],
        'Injury': [int(request.form['Injury'])],
        'Mental': [int(request.form['Mental'])],
        'Pain': [int(request.form['Pain'])],
        'NRS_pain': [int(request.form['NRS_pain'])],
        'SBP': [float(request.form['SBP'])],
        'DBP': [float(request.form['DBP'])],
        'HR': [float(request.form['HR'])],
        'RR': [float(request.form['RR'])],
        'BT': [float(request.form['BT'])],
        'Saturation': [float(request.form['Saturation'])]
    }
    # Convert to pandas DataFrame
    input_df = pd.DataFrame.from_dict(input_data)
    # Convert categorical variables into dummy variables
    input_df = pd.get_dummies(input_df)
    # Predict the label for the new data point
    index = model.predict(input_df)[0]
    return jsonify(f'Predicted Triage Category: {labels[index]}')

















if __name__ == "__main__":

    # run the flask app
    app.run()
