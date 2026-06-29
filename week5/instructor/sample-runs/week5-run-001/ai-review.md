# Fresh-context AI Review

## Blocking

None.

## Should Fix

None before classroom use.

## Optional

- `BookingConflictError` remains defined and mapped in `app/main.py` even though
  the new overlap path no longer raises it. It can remain for teaching clarity
  and backward-compatible error structure, but a production cleanup could remove
  it in a separate refactor.
- Add a test for a partial-overlap waitlist request if the instructor wants to
  discuss overlap versus exact-slot semantics.

## Questions For The Author

- Should promotion be exact same start/end only, or should it handle any
  overlapping waitlisted request? The task contract says "same room and time
  slot", so exact match is acceptable for this run.

## Review Decision

The diff stays within the approved scope, does not change dependencies or the
verification script, and includes tests for the main acceptance criteria.
