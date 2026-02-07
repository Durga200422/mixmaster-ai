from fastapi.testclient import TestClient
from mixmaster.main import app  # Fixed

client = TestClient(app)

def test_api_health_check():
    response = client.get("/api/v1/health")  # Prefix
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
