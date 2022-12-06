from fastapi.testclient import TestClient
# from .app.bmain import app
from .main import app
import pytest
from httpx import AsyncClient

client = TestClient(app)

@pytest.mark.integration
def test_backend_side():
    response = client.get("http://backend:8080/")
    assert response.status_code ==200
    assert response.json()["Hello"] =="hello from backend"

@pytest.mark.integration
def test_twitter_side():
    response = client.get("http://twitter:9090/")
    assert response.status_code ==200
    assert response.json()["Hello"] =="hello from backend"

@pytest.mark.integration
def test_analysis_side():
    response = client.get("http://textanalysis:7070/")
    assert response.status_code ==200
    assert response.json()["Hello"] =="hello from backend"

@pytest.mark.integration
def test_get_twiter():
    
    response = client.get("/twins/cloudflare")
    assert response.status_code ==200
    assert response.json()["share"] =="cloudflare"
    assert len(response.json()["tweet"])>0

@pytest.mark.integration
def test_get_analysis():
    response = client.get("/analysis/cloudflare")
    assert response.status_code ==200
    analysis = response.json()
    assert analysis['positive']>=0
    assert analysis['negative']>=0
