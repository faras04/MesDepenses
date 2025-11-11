# ml/train.py
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

def train_model():
    df = pd.read_csv("data/transactions.csv")
    df['text'] = (df['merchant'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

    X = df['text']
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)


    model = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ('clf', LogisticRegression(max_iter=300))
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("\n=== Rapport de performance ===")
    print(classification_report(y_test, preds))

    joblib.dump(model, "ml/model.pkl")
    print("✅ Modèle enregistré dans ml/model.pkl")

if __name__ == "__main__":
    train_model()
    