# tests/test_data_service.py
from app.services.data_service import data_service
import pandas as pd

def test_load_transactions():
    """Teste le chargement du CSV de transactions."""
    df = data_service.load_transactions()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert set(["merchant", "description", "amount"]).issubset(df.columns)
