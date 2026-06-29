from datetime import datetime

from pydantic import BaseModel

from app.models import BookingStatus


class RoomResponse(BaseModel):
    id: str
    name: str
    room_type: str
    capacity: int


class BookingCreateRequest(BaseModel):
    requester: str
    room_id: str
    start_time: datetime
    end_time: datetime


class BookingResponse(BaseModel):
    id: int
    room_id: str
    requester: str
    start_time: datetime
    end_time: datetime
    status: BookingStatus
    created_at: datetime
