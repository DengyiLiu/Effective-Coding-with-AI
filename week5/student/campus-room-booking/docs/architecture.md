# Architecture

The starter project is intentionally small and layered.

```text
app/main.py
  FastAPI routes and HTTP error mapping

app/schemas.py
  Request and response models

app/booking_service.py
  Booking rules, conflict detection, cancellation behavior

app/storage.py
  In-memory rooms and bookings

app/models.py
  Domain dataclasses and status enum
```

## Current Booking Flow

```text
POST /bookings
-> parse request
-> validate requester and time range
-> verify room exists
-> find confirmed bookings for same room
-> reject overlapping confirmed booking
-> create confirmed booking
```

## Current Cancellation Flow

```text
DELETE /bookings/{booking_id}
-> find booking
-> reject unknown booking
-> reject already-cancelled booking
-> mark booking cancelled
-> return updated booking
```

## Current Conflict Logic

Two time ranges overlap when:

```text
start_a < end_b and start_b < end_a
```

Adjacent bookings are allowed:

```text
10:00-11:00 and 11:00-12:00 do not overlap
```

Cancelled bookings do not block future bookings.

## Week 5 Feature Surface

The likely feature area is:

```text
app/models.py
app/booking_service.py
app/schemas.py
tests/
docs/api-contract.md
```

Students should not need to modify:

```text
scripts/verify.sh
requirements.txt
unrelated endpoints
```
