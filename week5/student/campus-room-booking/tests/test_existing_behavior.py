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


def test_list_bookings_returns_created_records_in_id_order():
    first = client.post("/bookings", json=booking_payload(requester="Alice"))
    second = client.post(
        "/bookings",
        json=booking_payload(
            requester="Bob",
            start_time="2026-07-01T11:00:00Z",
            end_time="2026-07-01T12:00:00Z",
        ),
    )
    assert first.status_code == 201
    assert second.status_code == 201

    response = client.get("/bookings")

    assert response.status_code == 200
    bookings = response.json()
    assert [booking["id"] for booking in bookings] == [1, 2]
    assert [booking["requester"] for booking in bookings] == ["Alice", "Bob"]
    assert all(booking["status"] == "confirmed" for booking in bookings)


def test_overlapping_request_is_rejected_and_does_not_create_second_booking():
    first = client.post("/bookings", json=booking_payload(requester="Alice"))
    assert first.status_code == 201

    conflict = client.post("/bookings", json=booking_payload(requester="Bob"))
    assert conflict.status_code == 409

    response = client.get("/bookings")
    bookings = response.json()
    assert len(bookings) == 1
    assert bookings[0]["requester"] == "Alice"
    assert bookings[0]["status"] == "confirmed"


def test_room_listing_remains_available_after_booking_changes():
    created = client.post("/bookings", json=booking_payload())
    assert created.status_code == 201
    cancelled = client.delete(f"/bookings/{created.json()['id']}")
    assert cancelled.status_code == 200

    response = client.get("/rooms")

    assert response.status_code == 200
    assert [room["id"] for room in response.json()] == ["study-a", "seminar-b", "lab-c"]
