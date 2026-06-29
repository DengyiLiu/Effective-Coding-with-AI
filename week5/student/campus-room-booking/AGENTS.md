# Repository Guidelines

## Project Structure

This is the Week 5 Campus Room Booking API starter. Source code is in `app/`,
tests are in `tests/`, docs are in `docs/`, and verification is handled by
`scripts/verify.sh`.

Important files to read before editing:

- `docs/api-contract.md`
- `docs/architecture.md`
- `docs/waitlist-spec.md`
- `tests/`
- `app/booking_service.py`

## Development Commands

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
```

## AI Coding Rules

- Do not implement before completing the workflow contract, reconnaissance,
  implementation plan, and human approval.
- Do not change endpoint names.
- Do not add dependencies without approval.
- Do not modify `scripts/verify.sh` without approval.
- Do not delete tests, weaken assertions, or skip tests to pass verification.
- Existing conflict-rejection tests may be updated only to assert the approved
  waitlist behavior.
- Preserve room listing, confirmed booking creation, and cancellation behavior
  unless the task contract explicitly changes it.

## Verification

Every implementation must pass:

```bash
bash scripts/verify.sh
```

Verification evidence must map tests back to acceptance criteria.
