import requests

payload = {
    "age": 35,
    "income": 50000,
    "loan_amount": 20000,
    "credit_score": 650,
    "num_defaults": 1,
    "employment_years": 5
}

response = requests.post("http://127.0.0.1:8000/predict", json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())