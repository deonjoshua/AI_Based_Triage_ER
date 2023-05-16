# import necessary libraries
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import (
    Flask,
    render_template,
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

@app.route("/form")
def form():
    return render_template("data_input.html")


#################################################
# API - Back End
#################################################

@app.route('/api/predict', methods=['POST'])
def predict():
    labels = ['Triage 1 - Resuscitation: 2mins', 'Triage 2 - Emergency: 10mins', 'Triage 3 - Urgent: 30min', 'Triage 4 - Semi-Urgent: 60mins', 'Triage 5 - Non-Urgent: 120mins']
    # Capture the inputs from the form
    input_data = {
        'Sex': [int(request.form['Sex'])],
        'Age': [int(request.form['Age'])],
        'Arrival mode': [str(request.form['Arrival mode'])],
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

    if input_data['Arrival mode'] == '1':
        input_data['Arrival mode_1'] = 1
        input_data['Arrival mode_2'] = 0
        input_data['Arrival mode_3'] = 0
        input_data['Arrival mode_4'] = 0
        input_data['Arrival mode_Other'] = 0

    elif input_data['Arrival mode'] == '2':
        input_data['Arrival mode_1'] = 0
        input_data['Arrival mode_2'] = 1
        input_data['Arrival mode_3'] = 0
        input_data['Arrival mode_4'] = 0
        input_data['Arrival mode_Other'] = 0

    elif input_data['Arrival mode'] == '3':
        input_data['Arrival mode_1'] = 0
        input_data['Arrival mode_2'] = 0
        input_data['Arrival mode_3'] = 1
        input_data['Arrival mode_4'] = 0
        input_data['Arrival mode_Other'] = 0

    elif input_data['Arrival mode'] == '4':
        input_data['Arrival mode_1'] = 0
        input_data['Arrival mode_2'] = 0
        input_data['Arrival mode_3'] = 0
        input_data['Arrival mode_4'] = 1
        input_data['Arrival mode_Other'] = 0

    else:
        input_data['Arrival mode_1'] = 0
        input_data['Arrival mode_2'] = 0
        input_data['Arrival mode_3'] = 0
        input_data['Arrival mode_4'] = 0
        input_data['Arrival mode_Other'] = 1


    # Convert to pandas DataFrame
    input_df = pd.DataFrame.from_dict(input_data)

    input_df = input_df.drop(['Arrival mode'], axis=1)

    scaler = StandardScaler()
    input_df[['SBP', 'DBP', 'HR', 'RR', 'BT', 'Saturation','Age']] = scaler.fit_transform(input_df[['SBP', 'DBP', 'HR', 'RR', 'BT', 'Saturation','Age']])
    
    # Predict the label for the new data point
    index = model.predict(input_df)[0]
    prediction = labels[index-1]
    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":

    # run the flask app
    app.run()
