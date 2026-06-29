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


def test_cancel_confirmed_booking_marks_it_cancelled():
    created = client.post("/bookings", json=booking_payload())
    booking_id = created.json()["id"]

    response = client.delete(f"/bookings/{booking_id}")

    assert response.status_code == 200
    cancelled = response.json()
    assert cancelled["id"] == booking_id
    assert cancelled["status"] == "cancelled"


def test_cancelled_booking_no_longer_blocks_same_slot():
    created = client.post("/bookings", json=booking_payload(requester="Alice"))
    booking_id = created.json()["id"]
    cancelled = client.delete(f"/bookings/{booking_id}")
    assert cancelled.status_code == 200

    response = client.post("/bookings", json=booking_payload(requester="Bob"))

    assert response.status_code == 201
    assert response.json()["status"] == "confirmed"


def test_cancel_unknown_booking_returns_404():
    response = client.delete("/bookings/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "booking 999 does not exist"


def test_cancel_already_cancelled_booking_returns_409():
    created = client.post("/bookings", json=booking_payload())
    booking_id = created.json()["id"]
    first_cancel = client.delete(f"/bookings/{booking_id}")
    assert first_cancel.status_code == 200

    response = client.delete(f"/bookings/{booking_id}")

    assert response.status_code == 409
    assert response.json()["detail"] == f"booking {booking_id} is already cancelled"
