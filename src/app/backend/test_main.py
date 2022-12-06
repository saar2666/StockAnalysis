from fastapi.testclient import TestClient
from .main import app
import pytest
from httpx import AsyncClient

client = TestClient(app)

def test_get_twiter():
    response = client.get("/twins/cloudflare")
    assert response.status_code ==200
    assert response.json()["share"] =="cloudflare"
    assert len(response.json()["tweet"])>0

def test_get_analysis():
    response = client.get("/analysis/cloudflare")
    assert response.status_code ==200
    assert response.json() == {"stock": "cloudflare", "positive": 200,"negative":300 }
