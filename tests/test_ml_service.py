# tests/test_ml_service.py
from app.services.ml_service import ml_service

def test_ml_prediction_type():
    """Vérifie que la prédiction retourne une chaîne de caractères."""
    result = ml_service.predict_category("Amazon", "Achat en ligne Amazon.fr")
    assert isinstance(result, str)
