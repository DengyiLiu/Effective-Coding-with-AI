# Reconnaissance

## Relevant Files

- `app/main.py` maps service errors to HTTP responses.
- `app/models.py` defines `BookingStatus` and the `Booking` dataclass.
- `app/booking_service.py` owns booking creation, overlap checks, and cancellation.
- `app/storage.py` stores rooms and bookings in memory.
- `app/schemas.py` exposes booking status in API responses.
- `tests/test_booking_create.py` covers booking creation and overlap behavior.
- `tests/test_booking_cancel.py` covers cancellation behavior.
- `tests/test_existing_behavior.py` contains regression coverage.
- `docs/api-contract.md` documents the public API behavior.
- `scripts/verify.sh` runs `python -m pytest`.

## Current Booking Flow

`POST /bookings` validates requester and time range, checks the room exists,
looks for confirmed bookings in the same room, rejects overlap with `409`, and
otherwise creates a confirmed booking.

## Current Cancellation Flow

`DELETE /bookings/{booking_id}` finds the booking, rejects unknown or already
cancelled bookings, marks the booking as cancelled, saves it, and returns the
cancelled booking.

## Current Conflict Logic

Overlap is detected with:

```text
start_a < end_b and start_b < end_a
```

Only confirmed bookings block new bookings. Cancelled bookings do not block.

## Existing Tests

The suite verifies room listing, confirmed booking creation, overlap rejection,
adjacent bookings, different-room bookings, invalid inputs, cancellation, and
booking listing order.

## Verification Command

```bash
bash scripts/verify.sh
```

## Likely Risks

- Forgetting to promote the earliest waitlisted booking.
- Promoting after cancelling a waitlisted booking.
- Deleting or weakening the old conflict regression instead of updating it to
  assert the approved waitlist behavior.
- Changing endpoint names or response shape unnecessarily.
- Letting waitlisted bookings block other waitlisted requests.

## Minimal Edit Scope

- `app/models.py`
- `app/booking_service.py`
- `tests/test_booking_create.py`
- `tests/test_existing_behavior.py`
- `tests/test_waitlist.py`
- `docs/api-contract.md`
- `docs/architecture.md`
- `README.md` for instructor solution labeling

No dependency or verification script changes are needed.
