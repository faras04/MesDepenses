# app/services/ml_service.py
import joblib
from pathlib import Path

MODEL_PATH = Path("ml/model.pkl")

class MLService:
    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError("⚠️ Le modèle ML n'a pas été trouvé. Entraîne-le d'abord (ml/train.py).")
        self.model = joblib.load(MODEL_PATH)

    def predict_category(self, merchant: str, description: str) -> str:
        """Prédit une catégorie à partir des champs texte."""
        text = f"{merchant} {description}".lower()
        return self.model.predict([text])[0]

ml_service = MLService()
