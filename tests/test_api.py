from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenue" in response.json()["message"]

def test_categorize_endpoint():
    payload = [
        {"merchant": "Uber", "description": "Course Paris", "amount": -12.3}
    ]
    response = client.post("/api/categorize", json=payload)
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert "predicted_category" in result[0]
