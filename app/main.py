# app/main.py
from fastapi import FastAPI
from app.routes import categorize

app = FastAPI(title="Mes Dépenses API", version="1.0")

# Inclusion des routes
app.include_router(categorize.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l’API Mes Dépenses 🚀"}
