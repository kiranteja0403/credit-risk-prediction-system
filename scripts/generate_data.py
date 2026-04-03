import os
import pandas as pd
import numpy as np

np.random.seed(42)

num_rows = 5000

data = pd.DataFrame({
    "age": np.random.randint(21, 65, num_rows),
    "income": np.random.randint(20000, 150000, num_rows),
    "loan_amount": np.random.randint(1000, 50000, num_rows),
    "credit_score": np.random.randint(300, 850, num_rows),
    "num_defaults": np.random.randint(0, 5, num_rows),
    "employment_years": np.random.randint(0, 30, num_rows)
})

risk_score = (
    (data["loan_amount"] / data["income"]) * 2 +
    (700 - data["credit_score"]) / 400 +
    data["num_defaults"] * 0.5 -
    data["employment_years"] * 0.02
)

data["risk"] = (risk_score > 1.5).astype(int)

os.makedirs("data/raw", exist_ok=True)
data.to_csv("data/raw/credit_data.csv", index=False)

print("Dataset created successfully")
print(data.head())