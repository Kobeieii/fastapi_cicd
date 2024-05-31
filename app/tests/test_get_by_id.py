from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_get_by_id_1_should_response_200():
    response = client.get("/pets/1", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "Toob",
        "type": "Dog",
        "sound": "Bark",
        "id": 1,
        "created_at": "2024-05-30T10:50:05",
        "updated_at": "2024-05-30T10:50:05"
    }

def test_get_by_id_4_should_response_404():
    response = client.get("/pets/4", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}