from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_rooms_returns_seeded_rooms():
    response = client.get("/rooms")

    assert response.status_code == 200
    rooms = response.json()
    assert len(rooms) == 3
    assert rooms[0] == {
        "id": "study-a",
        "name": "Study Room A",
        "room_type": "study",
        "capacity": 4,
    }


def test_room_listing_shape_is_stable():
    response = client.get("/rooms")

    assert response.status_code == 200
    room = response.json()[0]
    assert set(room.keys()) == {"id", "name", "room_type", "capacity"}
