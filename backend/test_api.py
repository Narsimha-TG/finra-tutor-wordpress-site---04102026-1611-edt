import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_theme_settings():
    response = client.get("/wp-json/finra/v1/theme-settings")
    assert response.status_code == 200
    assert "theme_mode" in response.json()

def test_get_seo_metadata():
    response = client.get("/wp-json/finra/v1/seo-metadata")
    assert response.status_code == 200
    assert "seo_keywords" in response.json()

def test_toggle_theme_success():
    payload = {"theme_mode": "dark", "user_id": 1}
    response = client.post("/wp-json/finra/v1/toggle-theme", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["new_mode"] == "dark"

def test_toggle_theme_invalid_data():
    # Testing schema validation
    payload = {"invalid_field": "data"}
    response = client.post("/wp-json/finra/v1/toggle-theme", json=payload)
    assert response.status_code == 422