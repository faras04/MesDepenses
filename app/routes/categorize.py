# app/routes/categorize.py
from fastapi import APIRouter
from app.models.transaction import TransactionIn, TransactionOut
from app.services.ml_service import ml_service

router = APIRouter(prefix="/api", tags=["Catégorisation"])

@router.post("/categorize", response_model=list[TransactionOut])
def categorize_transactions(transactions: list[TransactionIn]):
    """Endpoint de catégorisation des transactions."""
    results = []
    for t in transactions:
        cat = ml_service.predict_category(t.merchant, t.description)
        results.append(TransactionOut(
            merchant=t.merchant,
            description=t.description,
            amount=t.amount,
            predicted_category=cat
        ))
    return results
