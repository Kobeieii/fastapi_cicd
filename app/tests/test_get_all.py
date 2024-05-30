from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_get_all_should_response_200():
    response = client.get("/pets", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Toob",
            "type": "Dog",
            "sound": "Bark",
            "id": 1,
            "created_at": "2024-05-30T10:50:05",
            "updated_at": "2024-05-30T10:50:05"
        },
        {
            "name": "Sood Loar",
            "type": "Cat",
            "sound": "Meow",
            "id": 2,
            "created_at": "2024-05-30T10:50:05",
            "updated_at": "2024-05-30T10:50:05"
        },
        {
            "name": "Jibb",
            "type": "Bird",
            "sound": "Chirp",
            "id": 3,
            "created_at": "2024-05-30T10:50:05",
            "updated_at": "2024-05-30T10:50:05"
        }
    ]