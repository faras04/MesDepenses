# app/services/data_service.py
import pandas as pd

class DataService:
    def __init__(self, csv_path: str = "data/transactions.csv"):
        self.csv_path = csv_path

    def load_transactions(self) -> pd.DataFrame:
        """Charge les transactions depuis le CSV local."""
        df = pd.read_csv(self.csv_path)
        df['merchant'] = df['merchant'].fillna('')
        df['description'] = df['description'].fillna('')
        df['amount'] = df['amount'].astype(float)
        return df

data_service = DataService()
