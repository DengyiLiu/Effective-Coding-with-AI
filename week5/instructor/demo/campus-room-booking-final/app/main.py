from typing import List

from fastapi import FastAPI, HTTPException, status

from app.booking_service import (
    BookingAlreadyCancelledError,
    BookingConflictError,
    BookingNotFoundError,
    InvalidBookingRequestError,
    RoomNotFoundError,
    cancel_booking,
    create_booking,
    list_bookings,
    list_rooms,
)
from app.models import Booking, Room
from app.schemas import BookingCreateRequest, BookingResponse, RoomResponse

app = FastAPI(title="Campus Room Booking API")


@app.get("/rooms", response_model=List[RoomResponse])
def get_rooms() -> List[RoomResponse]:
    return [_room_response(room) for room in list_rooms()]


@app.get("/bookings", response_model=List[BookingResponse])
def get_bookings() -> List[BookingResponse]:
    return [_booking_response(booking) for booking in list_bookings()]


@app.post("/bookings", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def post_booking(request: BookingCreateRequest) -> BookingResponse:
    try:
        booking = create_booking(
            requester=request.requester,
            room_id=request.room_id,
            start_time=request.start_time,
            end_time=request.end_time,
        )
    except InvalidBookingRequestError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except RoomNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except BookingConflictError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    return _booking_response(booking)


@app.delete("/bookings/{booking_id}", response_model=BookingResponse)
def delete_booking(booking_id: int) -> BookingResponse:
    try:
        booking = cancel_booking(booking_id)
    except BookingNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except BookingAlreadyCancelledError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    return _booking_response(booking)


def _room_response(room: Room) -> RoomResponse:
    return RoomResponse(
        id=room.id,
        name=room.name,
        room_type=room.room_type,
        capacity=room.capacity,
    )


def _booking_response(booking: Booking) -> BookingResponse:
    return BookingResponse(
        id=booking.id,
        room_id=booking.room_id,
        requester=booking.requester,
        start_time=booking.start_time,
        end_time=booking.end_time,
        status=booking.status,
        created_at=booking.created_at,
    )
