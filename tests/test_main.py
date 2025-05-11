from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={
        "name": "Stylo",
        "price": 2.5,
        "in_stock": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Stylo"
    assert data["price"] == 2.5
    assert data["in_stock"] is True

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
