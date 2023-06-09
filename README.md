# AI-Based Triage System for Emergency Departments

![image](https://github.com/deonjoshua/AI_Based_Triage_ER/assets/117792685/483cf2cb-647d-4a8d-95f3-017fc7996fd5)


This project aims to develop an AI-based triage system to aid healthcare professionals in emergency departments. The system uses machine learning algorithms to classify and prioritize patients based on the severity of their conditions.

## Project Overview

The goal of this project is to:

1. Improve efficiency in emergency departments
2. Reduce waiting times for patients
3. Improve patient outcomes by ensuring that critical cases are attended to promptly

This project uses the KTAS (Korean Triage and Acuity Scale) scoring system as a basis for triage.

## Data Preprocessing

Our dataset includes vital signs, presenting symptoms, medical history, level of consciousness, and pain scale. The preprocessing steps include:

- Identifying and handling null values
- Identifying important variables for model training
- Identifying categorical and numerical values
- Scaling numerical values

<img width="960" alt="image" src="https://github.com/deonjoshua/AI_Based_Triage_ER/assets/117792685/f42e2ce0-9c28-4de9-8d8f-b3c30ddbee3d">

## Machine Learning Models

We use two primary models in this project:

- Random Forest: A supervised learning model that finds the hyperplane which best separates the different classes of patients.
![Wiiner](https://github.com/deonjoshua/AI_Based_Triage_ER/assets/117792685/91049e1b-8210-47f5-b41b-258857cab514)

- K-Nearest Neighbors (KNN): A supervised learning model that classifies patients based on the similarity of their features to those of patients in the training dataset.
![Picture 1](https://github.com/deonjoshua/AI_Based_Triage_ER/assets/117792685/65108a11-fa27-492d-9b5e-5fae121c9342)

## Output

<img width="1440" alt="Screenshot 2023-05-16 at 9 08 29 pm" src="https://github.com/deonjoshua/AI_Based_Triage_ER/assets/117792685/bbd8595b-010a-4a44-9f06-34107246f8dc">


## Running the Scripts

- Create a new conda environment for this app with the following code:

- All of our project dependencies will be installed in this environment.

- Note: This should contain only python 3.7—and not anaconda.
```bash
conda create -n ai_triage_env python=3.7
```
- Activate this new environment before proceeding.
```bash
conda activate ai_triage_env

# Note: If you run into issues, try the following command instead.
source activate ai_triage_env
```

- Install the libraries into your new environment.
```bash
# install pip packages listed in requirements file 
pip install -r requirements.txt
```
- Next, to make the run.sh file executable, run the following command:
```bash
chmod a+x run.sh
```
You can test the application by running the following in your command line.
```bash
./run.sh
```
- Navigate to 127.0.0.1:5000 to view your webpage and test out the app locally.

- This starter code uses a .csv file as the database.
