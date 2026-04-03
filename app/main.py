import joblib
import pandas as pd
from fastapi import FastAPI
from app.schemas import CreditRiskInput

app = FastAPI(title="Credit Risk Prediction API")

model = joblib.load("models/credit_risk_model.pkl")


@app.get("/")
def home():
    return {"message": "Credit Risk Prediction API is running"}


@app.post("/predict")
def predict_risk(data: CreditRiskInput):
    input_data = pd.DataFrame(
        [
            {
                "age": data.age,
                "income": data.income,
                "loan_amount": data.loan_amount,
                "credit_score": data.credit_score,
                "num_defaults": data.num_defaults,
                "employment_years": data.employment_years,
            }
        ]
    )

    prediction = model.predict(input_data)[0]

    try:
        probability = model.predict_proba(input_data)[0][1]
        if pd.isna(probability):
            probability = 0.0
    except Exception:
        probability = 0.0

    risk_label = "High Risk" if int(prediction) == 1 else "Low Risk"

    return {
        "predicted_risk": int(prediction),
        "risk_label": risk_label,
        "risk_probability": round(float(probability), 4),
    }