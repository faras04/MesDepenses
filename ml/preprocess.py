# ml/preprocess.py
import pandas as pd

def load_transactions(path: str) -> pd.DataFrame:
    """Charge et nettoie les transactions depuis un CSV."""
    df = pd.read_csv(path)
    df['merchant'] = df['merchant'].fillna('')
    df['description'] = df['description'].fillna('')
    df['text'] = (df['merchant'] + ' ' + df['description']).str.lower()
    df['amount'] = df['amount'].astype(float)
    return df
