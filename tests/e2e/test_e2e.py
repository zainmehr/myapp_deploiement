import os
import requests

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8080")


def test_application_is_available():
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_who_endpoint():
    response = requests.get(f"{BASE_URL}/who", timeout=5)
    assert response.status_code == 200
    assert response.text.strip() != ""


def test_create_then_list_task():
    created = requests.post(f"{BASE_URL}/tasks", json={"title": "Tâche E2E"}, timeout=5)
    assert created.status_code == 201
    task_id = created.json()["id"]

    listing = requests.get(f"{BASE_URL}/tasks", timeout=5)
    assert listing.status_code == 200
    assert any(t["id"] == task_id and t["title"] == "Tâche E2E" for t in listing.json())


def test_invalid_task_is_rejected():
    response = requests.post(f"{BASE_URL}/tasks", json={"title": ""}, timeout=5)
    assert response.status_code == 400