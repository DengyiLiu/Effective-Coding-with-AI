from datetime import datetime, timezone
from typing import Iterable

from app import storage
from app.models import Booking, BookingStatus


class BookingServiceError(Exception):
    """Base error for booking service failures."""


class InvalidBookingRequestError(BookingServiceError):
    pass


class RoomNotFoundError(BookingServiceError):
    pass


class BookingConflictError(BookingServiceError):
    pass


class BookingNotFoundError(BookingServiceError):
    pass


class BookingAlreadyCancelledError(BookingServiceError):
    pass


def create_booking(
    requester: str,
    room_id: str,
    start_time: datetime,
    end_time: datetime,
) -> Booking:
    requester = requester.strip()
    if not requester:
        raise InvalidBookingRequestError("requester is required")

    if end_time <= start_time:
        raise InvalidBookingRequestError("end_time must be after start_time")

    if storage.get_room(room_id) is None:
        raise RoomNotFoundError(f"room '{room_id}' does not exist")

    status = BookingStatus.CONFIRMED
    existing = _confirmed_bookings_for_room(room_id)
    if any(_times_overlap(start_time, end_time, booking.start_time, booking.end_time) for booking in existing):
        status = BookingStatus.WAITLISTED

    booking = Booking(
        id=storage.next_booking_id(),
        room_id=room_id,
        requester=requester,
        start_time=start_time,
        end_time=end_time,
        status=status,
        created_at=datetime.now(timezone.utc),
    )
    return storage.save_booking(booking)


def cancel_booking(booking_id: int) -> Booking:
    booking = storage.get_booking(booking_id)
    if booking is None:
        raise BookingNotFoundError(f"booking {booking_id} does not exist")

    if booking.status == BookingStatus.CANCELLED:
        raise BookingAlreadyCancelledError(f"booking {booking_id} is already cancelled")

    was_confirmed = booking.status == BookingStatus.CONFIRMED
    booking.status = BookingStatus.CANCELLED
    cancelled = storage.save_booking(booking)

    if was_confirmed:
        waitlisted = _earliest_waitlisted_for_same_slot(cancelled)
        if waitlisted is not None:
            waitlisted.status = BookingStatus.CONFIRMED
            storage.save_booking(waitlisted)

    return cancelled


def list_bookings() -> list[Booking]:
    return storage.list_bookings()


def list_rooms():
    return storage.list_rooms()


def _confirmed_bookings_for_room(room_id: str) -> Iterable[Booking]:
    return (
        booking
        for booking in storage.list_bookings()
        if booking.room_id == room_id and booking.status == BookingStatus.CONFIRMED
    )


def _earliest_waitlisted_for_same_slot(cancelled_booking: Booking) -> Booking | None:
    candidates = (
        booking
        for booking in storage.list_bookings()
        if booking.room_id == cancelled_booking.room_id
        and booking.start_time == cancelled_booking.start_time
        and booking.end_time == cancelled_booking.end_time
        and booking.status == BookingStatus.WAITLISTED
    )
    return min(candidates, key=lambda booking: booking.id, default=None)


def _times_overlap(
    start_a: datetime,
    end_a: datetime,
    start_b: datetime,
    end_b: datetime,
) -> bool:
    return start_a < end_b and start_b < end_a
