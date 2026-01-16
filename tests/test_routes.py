from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_flow():
    r = client.post("/brands", json={
        "brand_name": "Apple",
        "tone_keywords": ["clean"],
        "samples": ["Beautiful design"]
    })
    assert r.status_code == 200

    r = client.get("/brands")
    assert "Apple" in r.json()

    r = client.post("/check-tone", json={
        "brand_name": "Apple",
        "text": "Beautiful clean design"
    })
    assert r.status_code == 200
