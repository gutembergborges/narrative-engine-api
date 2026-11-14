"""API test for the health endpoint.

TestClient calls the app in-process: no server, no network, no Docker needed.
Docs: https://fastapi.tiangolo.com/tutorial/testing/
"""

from fastapi.testclient import TestClient

from narrative_engine.api.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
