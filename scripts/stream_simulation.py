import time
import random
import requests

sample_records = [
    {
        "age": 32,
        "income": 45000,
        "loan_amount": 18000,
        "credit_score": 620,
        "num_defaults": 1,
        "employment_years": 4
    },
    {
        "age": 45,
        "income": 90000,
        "loan_amount": 12000,
        "credit_score": 780,
        "num_defaults": 0,
        "employment_years": 12
    },
    {
        "age": 27,
        "income": 38000,
        "loan_amount": 25000,
        "credit_score": 540,
        "num_defaults": 2,
        "employment_years": 2
    },
    {
        "age": 51,
        "income": 110000,
        "loan_amount": 30000,
        "credit_score": 710,
        "num_defaults": 0,
        "employment_years": 18
    }
]

api_url = "http://127.0.0.1:8000/predict"

print("Starting real-time credit risk simulation...\n")

for i in range(10):
    record = random.choice(sample_records)

    response = requests.post(api_url, json=record)

    print(f"Request {i + 1}")
    print("Input:", record)
    print("Prediction:", response.json())
    print("-" * 60)

    time.sleep(2)