# AI-Based Triage System for Emergency Departments

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

## Machine Learning Models

We use two primary models in this project:

- K-Nearest Neighbors (KNN): A supervised learning model that classifies patients based on the similarity of their features to those of patients in the training dataset.
- Random Forest: A supervised learning model that finds the hyperplane which best separates the different classes of patients.

## Running the Scripts

The scripts for this project are written in Python and are contained in .sh files. To run these scripts, navigate to the project directory in your terminal and execute the following commands:

```bash
chmod +x run.sh
./run.sh
