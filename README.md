
---

Real-Time Credit Risk Prediction System

Author: Kiran Teja

---

Project Overview

This project is a complete end-to-end machine learning system that predicts whether a customer is a low risk or high risk for credit approval. It is designed in a simple and practical way to reflect how real-world ML systems are built and used.

---

How the Project Works

The project is built step by step in a logical flow.

First, synthetic data is generated to simulate real customer financial data.
Then, multiple machine learning models are trained using this data.
The models are compared and the best-performing model is selected.
The selected model is saved and used for predictions.
A FastAPI-based API is created for real-time predictions.
Batch predictions are supported using CSV files.
Finally, a real-time simulation script sends continuous data to the API.

---

Approach and Logic

The system predicts credit risk using features such as age, income, loan amount, credit score, number of defaults, and employment years.

These inputs are processed using machine learning models to classify customers into Low Risk or High Risk.

Three models are used:
Logistic Regression
Random Forest
XGBoost

XGBoost performs the best and is used as the final model.

The system supports:
Real-time predictions using API
Batch predictions using files
Simulated real-time streaming

---

Project Structure

credit-risk-prediction-system/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── data/
│   └── raw/
│       ├── credit_data.csv
│       └── batch_predictions.csv
│
├── models/
│   └── credit_risk_model.pkl
│
├── scripts/
│   ├── generate_data.py
│   ├── train_model.py
│   ├── batch_score.py
│   ├── stream_simulation.py
│   └── test_api.py
│
├── .gitignore
├── README.md
└── venv/

---

Setup Instructions

Open terminal inside the project folder.

Create virtual environment:

python -m venv venv

Use this command to run Python from virtual environment:

.\venv\Scripts\python.exe

Install dependencies:

.\venv\Scripts\python.exe -m pip install pandas numpy scikit-learn xgboost fastapi uvicorn joblib requests

---

How to Run the Project

Step 1: Generate Dataset

.\venv\Scripts\python.exe scripts\generate_data.py

This creates the dataset in data/raw/credit_data.csv

---

Step 2: Train Model

.\venv\Scripts\python.exe scripts\train_model.py

This trains models and saves the best model in the models folder.

---

Step 3: Run Batch Prediction

.\venv\Scripts\python.exe scripts\batch_score.py

This generates predictions and creates batch_predictions.csv

---

Step 4: Start API Server

.\venv\Scripts\python.exe -m uvicorn app.main:app --reload

Open browser:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

Step 5: Test API Using Script

.\venv\Scripts\python.exe scripts\test_api.py

This sends a request and prints the prediction.

---

Step 6: Run Real-Time Simulation

.\venv\Scripts\python.exe scripts\stream_simulation.py

This simulates real-time incoming data and predictions.

---

API Input Example

{
"age": 35,
"income": 50000,
"loan_amount": 20000,
"credit_score": 650,
"num_defaults": 1,
"employment_years": 5
}

---

API Output Example

{
"predicted_risk": 0,
"risk_label": "Low Risk",
"risk_probability": 0.1064
}

---

Key Highlights

End-to-end machine learning pipeline
Multiple model training and comparison
Real-time API using FastAPI
Batch prediction support
Real-time simulation without Kafka
Simple and clean architecture

---

Future Improvements

Add database integration
Deploy on cloud
Add Docker support
Integrate Kafka for real streaming
Build UI dashboard

---

This project demonstrates how a real-world credit risk prediction system can be designed, trained, and deployed in a simple and scalable way.

---
