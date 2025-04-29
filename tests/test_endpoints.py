# Directory: project/tests/test_endpoints.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_itinerary():
    response = client.post(
        "/itineraries/",
        json={
            "name": "Holiday in Phuket",
            "days": []
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Holiday in Phuket"

def test_get_itineraries():
    response = client.get("/itineraries/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)