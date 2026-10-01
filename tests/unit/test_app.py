import pytest
from app import create_app, WHO


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_who_returns_name(client):
    response = client.get("/who")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == WHO


def test_tasks_empty_at_start(client):
    assert client.get("/tasks").get_json() == []


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Réviser"})
    assert response.status_code == 201
    assert response.get_json() == {"id": 1, "title": "Réviser"}


def test_create_task_without_title_fails(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400