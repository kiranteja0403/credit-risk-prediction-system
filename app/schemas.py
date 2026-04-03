from pydantic import BaseModel


class CreditRiskInput(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int
    num_defaults: int
    employment_years: int