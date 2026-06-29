# Campus Room Booking API Starter Project Spec

This file defines the intended starter project for Week 5. It is a specification,
not the implementation.

## Purpose

The starter project should be realistic enough to require careful AI-assisted
change management, but small enough for a 90-minute implementation lab.

The project should teach:

- reading an existing codebase before editing
- preserving existing behavior
- adding state transition logic
- writing regression tests
- using verification output as evidence
- reviewing a scoped diff

## Recommended Stack

```text
FastAPI
pytest
SQLite or in-memory repository
Python standard datetime handling
No frontend
No authentication
No external services
```

For classroom speed, an in-memory repository is acceptable. SQLite is acceptable
if setup is reliable on student machines.

## Starter Directory

```text
campus-room-booking/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   ├── booking_service.py
│   └── schemas.py
├── tests/
│   ├── test_rooms.py
│   ├── test_booking_create.py
│   ├── test_booking_cancel.py
│   └── test_existing_behavior.py
├── scripts/
│   └── verify.sh
├── docs/
│   ├── architecture.md
│   ├── api-contract.md
│   └── commands.md
├── README.md
└── requirements.txt
```

## Baseline Behavior

The starter project must pass before students begin the feature work.

Required behavior:

```text
GET /rooms
-> returns available rooms

POST /bookings
-> creates a confirmed booking if the room/time is free

POST /bookings
-> rejects overlapping booking for the same room/time

DELETE /bookings/{booking_id}
-> cancels an existing confirmed booking

GET /bookings
-> returns current bookings
```

Baseline verification:

```bash
bash scripts/verify.sh
```

## Feature Request

```text
Currently, when a room is already booked for a requested time slot,
the API rejects the request.

We want the system to support a waitlist.

If a user requests a room/time slot that is already booked,
the request should be stored as waitlisted instead of rejected.

If the confirmed booking is cancelled,
the earliest waitlisted booking for the same room/time slot
should be promoted to confirmed automatically.
```

## Acceptance Criteria

```text
AC1. A booking request for an available room/time slot creates a confirmed booking.

AC2. A booking request for an occupied room/time slot creates a waitlisted booking.

AC3. Waitlisted bookings preserve request order.

AC4. Cancelling a confirmed booking with no waitlist simply cancels the booking.

AC5. Cancelling a confirmed booking with a waitlist promotes the earliest waitlisted booking.

AC6. Cancelling a waitlisted booking does not promote anyone.

AC7. Existing room listing behavior remains unchanged.

AC8. Existing confirmed booking creation behavior remains unchanged.

AC9. Existing cancellation behavior remains backward compatible.

AC10. Tests cover available booking, conflict waitlisting, cancellation promotion,
no-waitlist cancellation, and waitlisted cancellation.
```

## Non-goals

```text
Do not add authentication.
Do not add email notifications.
Do not add payment or approval workflow.
Do not add recurring bookings.
Do not build a frontend.
Do not integrate Google Calendar.
Do not redesign the whole API.
Do not change unrelated endpoints.
Do not add external services.
Do not change the verification script without approval.
```

## Suggested Data Model

The starter can begin with a simple booking model:

```text
Booking
- id
- room_id
- requester
- start_time
- end_time
- status
- created_at
```

Baseline status may only use:

```text
confirmed
cancelled
```

The feature implementation can add:

```text
waitlisted
```

## API Compatibility Guidance

The starter API should already expose enough booking fields for students to
verify behavior through tests.

Preferred response fields:

```text
id
room_id
requester
start_time
end_time
status
```

If the baseline project does not expose `status`, the instructor should decide
whether adding it is approved in the task contract. The cleaner classroom path
is to expose `status` from the beginning so the feature does not require a
public response schema debate.

## Test Requirements

Starter tests should prove baseline behavior:

- list rooms
- create confirmed booking
- reject overlapping booking
- cancel confirmed booking
- list bookings

Feature tests should prove:

- available booking remains confirmed
- conflict creates waitlisted booking
- multiple waitlisted bookings preserve FIFO order
- cancelling confirmed booking promotes earliest waitlisted booking
- cancelling confirmed booking with no waitlist just cancels
- cancelling waitlisted booking does not promote anyone
- old room listing behavior still works

## Verification Script

`scripts/verify.sh` should be intentionally boring:

```bash
#!/usr/bin/env bash
set -euo pipefail
python -m pytest
```

Students may not modify this script unless the instructor explicitly approves
the change.

## Instructor Notes

The starter should include enough code to make reconnaissance meaningful:

- routes in `app/main.py`
- request/response schemas in `app/schemas.py`
- business logic in `app/booking_service.py`
- storage operations in `app/storage.py`
- model definitions in `app/models.py`

Avoid making the app too clever. The point is workflow control, not advanced
database design.
