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


def test_conflict_creates_waitlisted_booking():
    alice = client.post("/bookings", json=booking_payload(requester="Alice"))
    bob = client.post("/bookings", json=booking_payload(requester="Bob"))

    assert alice.status_code == 201
    assert alice.json()["status"] == "confirmed"
    assert bob.status_code == 201
    assert bob.json()["status"] == "waitlisted"


def test_waitlisted_bookings_preserve_request_order():
    client.post("/bookings", json=booking_payload(requester="Alice"))
    bob = client.post("/bookings", json=booking_payload(requester="Bob"))
    carla = client.post("/bookings", json=booking_payload(requester="Carla"))

    response = client.get("/bookings")

    assert response.status_code == 200
    bookings = response.json()
    assert [booking["requester"] for booking in bookings] == ["Alice", "Bob", "Carla"]
    assert bob.json()["id"] < carla.json()["id"]
    assert [booking["status"] for booking in bookings] == ["confirmed", "waitlisted", "waitlisted"]


def test_cancel_confirmed_booking_promotes_earliest_waitlisted_booking():
    alice = client.post("/bookings", json=booking_payload(requester="Alice"))
    client.post("/bookings", json=booking_payload(requester="Bob"))
    client.post("/bookings", json=booking_payload(requester="Carla"))

    cancelled = client.delete(f"/bookings/{alice.json()['id']}")
    response = client.get("/bookings")

    assert cancelled.status_code == 200
    assert cancelled.json()["status"] == "cancelled"
    bookings = response.json()
    assert [(booking["requester"], booking["status"]) for booking in bookings] == [
        ("Alice", "cancelled"),
        ("Bob", "confirmed"),
        ("Carla", "waitlisted"),
    ]


def test_cancel_confirmed_booking_with_no_waitlist_only_cancels():
    alice = client.post("/bookings", json=booking_payload(requester="Alice"))

    cancelled = client.delete(f"/bookings/{alice.json()['id']}")
    response = client.get("/bookings")

    assert cancelled.status_code == 200
    assert response.json()[0]["status"] == "cancelled"


def test_cancel_waitlisted_booking_does_not_promote_anyone():
    alice = client.post("/bookings", json=booking_payload(requester="Alice"))
    bob = client.post("/bookings", json=booking_payload(requester="Bob"))
    client.post("/bookings", json=booking_payload(requester="Carla"))

    cancelled_waitlist = client.delete(f"/bookings/{bob.json()['id']}")
    response = client.get("/bookings")

    assert cancelled_waitlist.status_code == 200
    bookings = response.json()
    assert [(booking["requester"], booking["status"]) for booking in bookings] == [
        ("Alice", "confirmed"),
        ("Bob", "cancelled"),
        ("Carla", "waitlisted"),
    ]
    assert alice.json()["status"] == "confirmed"
