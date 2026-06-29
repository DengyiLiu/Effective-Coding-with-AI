# Verification Report

## Command Run

```bash
bash scripts/verify.sh
```

## Result

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: instructor/demo/campus-room-booking-final
collected 20 items

tests/test_booking_cancel.py ....                                        [ 20%]
tests/test_booking_create.py ......                                      [ 50%]
tests/test_existing_behavior.py ...                                      [ 65%]
tests/test_rooms.py ..                                                   [ 75%]
tests/test_waitlist.py .....                                             [100%]

======================== 20 passed, 1 warning in 0.66s =========================
```

## Acceptance Criteria Mapping

| Acceptance Criterion | Evidence |
| --- | --- |
| AC1 available slot creates confirmed booking | `test_create_booking_for_available_slot_returns_confirmed_booking` |
| AC2 occupied slot creates waitlisted booking | `test_conflict_creates_waitlisted_booking` |
| AC3 waitlist preserves order | `test_waitlisted_bookings_preserve_request_order` |
| AC4 cancel confirmed with no waitlist | `test_cancel_confirmed_booking_with_no_waitlist_only_cancels` |
| AC5 cancel confirmed promotes earliest waitlisted | `test_cancel_confirmed_booking_promotes_earliest_waitlisted_booking` |
| AC6 cancel waitlisted does not promote | `test_cancel_waitlisted_booking_does_not_promote_anyone` |
| AC7 existing room listing unchanged | `test_list_rooms_returns_seeded_rooms`, `test_room_listing_shape_is_stable` |
| AC8 existing confirmed booking behavior unchanged | existing creation tests for available, adjacent, and different-room bookings |
| AC9 cancellation backward compatible | existing cancellation tests for cancel, unknown id, and already-cancelled id |
| AC10 tests cover main state transitions | `tests/test_waitlist.py` plus updated regression tests |

## Failures Encountered

- Initial dependency installation required network access in the local environment.
- No test failures after implementation.

## Fixes Made

- Added `waitlisted` status.
- Updated overlap creation behavior to save waitlisted bookings.
- Added promotion logic after confirmed cancellation.
- Updated old conflict regression tests to assert the approved waitlist behavior.
- Added focused waitlist tests.

## Remaining Limitations

- Promotion is defined for the same `room_id`, `start_time`, and `end_time`.
- The test client emits a third-party deprecation warning; it does not affect the feature.
