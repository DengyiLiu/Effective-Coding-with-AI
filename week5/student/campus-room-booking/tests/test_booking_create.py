from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def booking_payload(
    requester="Alice",
    room_id="study-a",
    start_time="2026-07-01T10:00:00Z",
    end_time="2026-07-01T11:00:00Z",
):
    return {
        "requester": requester,
        "room_id": room_id,
        "start_time": start_time,
        "end_time": end_time,
    }


def test_create_booking_for_available_slot_returns_confirmed_booking():
    response = client.post("/bookings", json=booking_payload())

    assert response.status_code == 201
    booking = response.json()
    assert booking["id"] == 1
    assert booking["room_id"] == "study-a"
    assert booking["requester"] == "Alice"
    assert booking["status"] == "confirmed"
    assert booking["start_time"] == "2026-07-01T10:00:00Z"
    assert booking["end_time"] == "2026-07-01T11:00:00Z"
    assert "created_at" in booking


def test_rejects_overlapping_booking_for_same_room():
    first = client.post("/bookings", json=booking_payload(requester="Alice"))
    assert first.status_code == 201

    response = client.post("/bookings", json=booking_payload(requester="Bob"))

    assert response.status_code == 409
    assert response.json()["detail"] == "room is already booked for that time slot"


def test_allows_adjacent_booking_for_same_room():
    first = client.post("/bookings", json=booking_payload(requester="Alice"))
    assert first.status_code == 201

    response = client.post(
        "/bookings",
        json=booking_payload(
            requester="Bob",
            start_time="2026-07-01T11:00:00Z",
            end_time="2026-07-01T12:00:00Z",
        ),
    )

    assert response.status_code == 201
    assert response.json()["status"] == "confirmed"


def test_allows_same_time_in_different_room():
    first = client.post("/bookings", json=booking_payload(room_id="study-a"))
    assert first.status_code == 201

    response = client.post(
        "/bookings",
        json=booking_payload(requester="Bob", room_id="seminar-b"),
    )

    assert response.status_code == 201
    assert response.json()["room_id"] == "seminar-b"
    assert response.json()["status"] == "confirmed"


def test_rejects_invalid_time_range():
    response = client.post(
        "/bookings",
        json=booking_payload(
            start_time="2026-07-01T11:00:00Z",
            end_time="2026-07-01T10:00:00Z",
        ),
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "end_time must be after start_time"


def test_rejects_unknown_room():
    response = client.post("/bookings", json=booking_payload(room_id="missing-room"))

    assert response.status_code == 404
    assert response.json()["detail"] == "room 'missing-room' does not exist"
