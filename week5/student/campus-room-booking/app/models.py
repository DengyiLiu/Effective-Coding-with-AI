from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BookingStatus(str, Enum):
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


@dataclass
class Room:
    id: str
    name: str
    room_type: str
    capacity: int


@dataclass
class Booking:
    id: int
    room_id: str
    requester: str
    start_time: datetime
    end_time: datetime
    status: BookingStatus
    created_at: datetime
