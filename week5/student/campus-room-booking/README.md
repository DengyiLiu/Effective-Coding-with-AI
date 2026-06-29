# Campus Room Booking API

This is the Week 5 starter project for AIM 5012.

The API is intentionally small but realistic enough to practice controlled
AI-assisted changes on an existing codebase.

## Current Behavior

The starter already supports:

- list rooms
- create confirmed bookings
- reject overlapping bookings
- cancel bookings
- list bookings
- run existing tests

## Week 5 Feature Request

Add waitlist and cancellation promotion:

```text
When a requested room/time slot is already booked, create a waitlisted booking.
When the confirmed booking is cancelled, promote the earliest waitlisted booking.
```

Do not implement the feature before completing the workflow artifacts.

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
scripts/
  verify.sh
docs/
  architecture.md
  api-contract.md
  waitlist-spec.md
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

The verification script compiles the app and runs the pytest suite.

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

Do not ask AI to implement the feature immediately.

Use the Week 5 workflow:

```text
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision
```

Before planning the feature, read:

- `docs/api-contract.md`
- `docs/architecture.md`
- `docs/waitlist-spec.md`
- `AGENTS.md`
