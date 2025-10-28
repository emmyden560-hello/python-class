import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_profile():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "user" in response.json()
    assert "fact" in response.json()
    assert "timestamp" in response.json()
