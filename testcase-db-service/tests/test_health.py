from fastapi.testclient import TestClient
from app.main import app
import pytest
from httpx import AsyncClient

client = TestClient(app)

@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
