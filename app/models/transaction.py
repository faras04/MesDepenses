# app/models/transaction.py
from pydantic import BaseModel

class TransactionIn(BaseModel):
    merchant: str
    description: str
    amount: float

class TransactionOut(TransactionIn):
    predicted_category: str
