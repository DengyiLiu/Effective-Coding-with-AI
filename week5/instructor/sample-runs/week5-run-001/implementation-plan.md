# Implementation Plan

## Goal

Add waitlist and cancellation promotion while preserving endpoint names,
response shape, room listing, confirmed booking creation, and existing
cancellation semantics.

## Proposed Files To Modify

| File | Change | Reason |
| --- | --- | --- |
| `app/models.py` | Add `waitlisted` booking status | Represent queued requests |
| `app/booking_service.py` | Create waitlisted booking on overlap; promote earliest waitlisted booking after confirmed cancellation | Core feature |
| `tests/test_booking_create.py` | Replace old conflict `409` assertion with waitlist assertion | Approved behavior change |
| `tests/test_existing_behavior.py` | Preserve regression shape while updating conflict expectation | Avoid hidden test weakening |
| `tests/test_waitlist.py` | Add feature tests for waitlist and promotion | Cover new state transitions |
| `docs/api-contract.md` | Document waitlist behavior | Keep public contract aligned |
| `docs/architecture.md` | Document new flow | Keep project context accurate |

## Files Not To Modify

- `scripts/verify.sh`
- `requirements.txt`
- endpoint names in `app/main.py`
- unrelated room behavior

## Acceptance Criteria Mapping

| AC | Implementation | Test Evidence |
| --- | --- | --- |
| AC1 | Keep no-overlap path as `confirmed` | `test_create_booking_for_available_slot_returns_confirmed_booking` |
| AC2 | Overlap sets status to `waitlisted` | `test_conflict_creates_waitlisted_booking` |
| AC3 | Preserve id order for waitlist entries | `test_waitlisted_bookings_preserve_request_order` |
| AC4 | Cancel confirmed with no waitlist only cancels | `test_cancel_confirmed_booking_with_no_waitlist_only_cancels` |
| AC5 | Cancel confirmed promotes earliest waitlisted | `test_cancel_confirmed_booking_promotes_earliest_waitlisted_booking` |
| AC6 | Cancel waitlisted does not promote | `test_cancel_waitlisted_booking_does_not_promote_anyone` |
| AC7 | Do not alter room routes | `test_list_rooms_returns_seeded_rooms` |
| AC8 | Keep available booking behavior | existing creation tests |
| AC9 | Keep cancellation errors and return shape | existing cancellation tests |
| AC10 | Add focused waitlist tests | `tests/test_waitlist.py` |

## Notes

Promotion should only consider waitlisted bookings with the same `room_id`,
`start_time`, and `end_time` as the cancelled confirmed booking.
