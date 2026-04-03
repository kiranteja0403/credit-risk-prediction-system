import os
import joblib
import pandas as pd

model = joblib.load("models/credit_risk_model.pkl")

data = pd.read_csv("data/raw/credit_data.csv")

X = data.drop("risk", axis=1)

predictions = model.predict(X)

try:
    probabilities = model.predict_proba(X)[:, 1]
except Exception:
    probabilities = [0.0] * len(predictions)

data["predicted_risk"] = predictions
data["risk_label"] = ["High Risk" if p == 1 else "Low Risk" for p in predictions]
data["risk_probability"] = probabilities

os.makedirs("data/raw", exist_ok=True)
data.to_csv("data/raw/batch_predictions.csv", index=False)

print("Batch prediction completed successfully")
print("Output file: data/raw/batch_predictions.csv")
print(data.head())