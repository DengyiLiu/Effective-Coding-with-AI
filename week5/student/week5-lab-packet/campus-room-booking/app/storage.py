from dataclasses import replace
from typing import Dict, List, Optional

from app.models import Booking, Room


DEFAULT_ROOMS = (
    Room(id="study-a", name="Study Room A", room_type="study", capacity=4),
    Room(id="seminar-b", name="Seminar Room B", room_type="seminar", capacity=12),
    Room(id="lab-c", name="Lab Room C", room_type="lab", capacity=24),
)

_rooms: Dict[str, Room] = {}
_bookings: Dict[int, Booking] = {}
_next_booking_id = 1


def reset_storage() -> None:
    global _rooms, _bookings, _next_booking_id
    _rooms = {room.id: replace(room) for room in DEFAULT_ROOMS}
    _bookings = {}
    _next_booking_id = 1


def list_rooms() -> List[Room]:
    return list(_rooms.values())


def get_room(room_id: str) -> Optional[Room]:
    return _rooms.get(room_id)


def list_bookings() -> List[Booking]:
    return sorted(_bookings.values(), key=lambda booking: booking.id)


def get_booking(booking_id: int) -> Optional[Booking]:
    return _bookings.get(booking_id)


def next_booking_id() -> int:
    global _next_booking_id
    booking_id = _next_booking_id
    _next_booking_id += 1
    return booking_id


def save_booking(booking: Booking) -> Booking:
    _bookings[booking.id] = booking
    return booking


reset_storage()
