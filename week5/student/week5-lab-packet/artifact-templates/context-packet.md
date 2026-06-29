# Context Packet

## Task

See `task-contract.yaml`.

## Project Summary

This is a FastAPI backend for campus room booking.

The app already supports:

- rooms
- confirmed bookings
- conflict rejection
- cancellation
- existing tests

## Important Files To Inspect

- `app/main.py`
- `app/models.py`
- `app/booking_service.py`
- `app/storage.py`
- `app/schemas.py`
- `tests/`
- `docs/api-contract.md`
- `docs/architecture.md`
- `docs/waitlist-spec.md`
- `AGENTS.md`
- `scripts/verify.sh`

## Verification Command

```bash
bash scripts/verify.sh
```

## Constraints

- Do not rewrite the whole project.
- Do not change endpoint names without approval.
- Do not add dependencies without approval.
- Do not delete or weaken existing tests.
- Preserve backward-compatible behavior.
- Do not modify `scripts/verify.sh` without approval.

## Current Goal

Add waitlist and cancellation promotion while preserving existing booking,
room listing, and cancellation behavior.
