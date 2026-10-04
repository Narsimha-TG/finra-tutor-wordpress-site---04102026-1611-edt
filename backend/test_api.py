import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tutor_profiles():
    response = client.get("/wp-json/finra/v1/tutor-profiles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert "tutor_name" in response.json()[0]

def test_create_booking_success():
    payload = {
        "tutor_id": 1,
        "student_name": "John Smith",
        "session_date": "2026-04-15"
    }
    response = client.post("/wp-json/finra/v1/booking", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "John Smith" in response.json()["message"]

def test_get_seo_metadata():
    response = client.get("/wp-json/finra/v1/seo-metadata")
    assert response.status_code == 200
    assert "title" in response.json()
    assert response.json()["title"] == "FINRA Exam Prep"

def test_invalid_booking_payload():
    payload = {"tutor_id": "invalid_id"}
    response = client.post("/wp-json/finra/v1/booking", json=payload)
    assert response.status_code == 422