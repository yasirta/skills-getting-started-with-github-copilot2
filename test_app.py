from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def setup_function():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]


def test_delete_signup_removes_participant():
    response = client.delete("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in activities["Chess Club"]["participants"]


def test_delete_signup_rejects_unknown_participant():
    response = client.delete("/activities/Chess Club/signup?email=student@mergington.edu")

    assert response.status_code == 400

def test_delete_signup_rejects_missing_activity():
    response = client.delete("/activities/Unknown Activity/signup?email=student@mergington.edu")

    assert response.status_code == 404
