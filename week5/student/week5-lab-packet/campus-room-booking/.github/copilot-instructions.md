# Copilot Instructions

This repository is a teaching starter for AIM 5012 Week 5. The goal is to
practice controlled AI coding, not to rewrite the application.

Before suggesting code changes, inspect:

- `docs/api-contract.md`
- `docs/architecture.md`
- `docs/waitlist-spec.md`
- `app/booking_service.py`
- `tests/`

Follow these rules:

- Keep changes minimal and within the approved file scope.
- Do not rename endpoints.
- Do not add dependencies.
- Do not edit `scripts/verify.sh` unless explicitly approved.
- Do not delete tests, weaken assertions, or mark tests skipped.
- Add or update tests for every acceptance criterion.
- Use `bash scripts/verify.sh` as the verification command.

For the Week 5 feature, conflict requests should become waitlisted bookings, and
cancelling a confirmed booking should promote the earliest waitlisted booking
for the same slot.
