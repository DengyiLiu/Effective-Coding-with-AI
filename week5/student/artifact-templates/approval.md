# Human Approval

## Plan Status

Approved with changes.

## Questions Asked Before Approval

1. Can this be done without changing endpoint names?
2. Can this be done without adding dependencies?
3. Which acceptance criterion is least covered by tests?
4. What is the smallest data model change?
5. What existing behavior might break?

## Required Changes Before Implementation

- Do not modify `scripts/verify.sh`.
- Do not delete existing tests.
- Existing conflict-rejection tests may be updated only to match the approved waitlist behavior.
- Do not change endpoint names.
- Add tests before or with implementation.
- Preserve backward-compatible response fields.

## Approved File Scope

AI may modify:

- `app/models.py`
- `app/booking_service.py`
- `app/schemas.py`
- `tests/test_booking_create.py` only for the approved conflict behavior change
- `tests/test_existing_behavior.py` only for the approved conflict behavior change
- `tests/test_waitlist.py`
- `docs/api-contract.md` if response schema changes

AI may not modify without additional approval:

- `scripts/verify.sh`
- `requirements.txt`
- unrelated endpoints
- unrelated tests

## Human Decision

I approve implementation only within the file scope above.
