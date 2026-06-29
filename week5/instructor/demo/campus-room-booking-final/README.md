# Campus Room Booking API

This is the Week 5 instructor demo final solution for AIM 5012.

The API is intentionally small but realistic enough to practice controlled
AI-assisted changes on an existing codebase.

## Current Behavior

This final solution supports:

- list rooms
- create confirmed bookings
- create waitlisted bookings for overlapping requests
- cancel bookings
- promote the earliest waitlisted booking when a confirmed booking is cancelled
- list bookings
- run existing tests

## Implemented Week 5 Feature

This version implements waitlist and cancellation promotion:

```text
When a requested room/time slot is already booked, create a waitlisted booking.
When the confirmed booking is cancelled, promote the earliest waitlisted booking.
```

The student starter project intentionally does not include this implementation.
Use this copy for instructor rehearsal, comparison, or live demo recovery.

## Project Structure

```text
app/
  main.py             FastAPI routes
  models.py           Domain dataclasses and status enum
  storage.py          In-memory repository
  booking_service.py  Booking and cancellation rules
  schemas.py          API request and response models
tests/
  test_rooms.py
  test_booking_create.py
  test_booking_cancel.py
  test_existing_behavior.py
  test_waitlist.py
scripts/
  verify.sh
docs/
  architecture.md
  api-contract.md
  commands.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Verify

```bash
source .venv/bin/activate
bash scripts/verify.sh
```

## Run Server

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Classroom Rule

Do not give this solution to students before they complete the workflow.

Students should reach this behavior through the Week 5 workflow:

```text
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision
```
