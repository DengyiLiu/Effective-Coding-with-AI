# Waitlist Feature Specification

This document defines the Week 5 target behavior. The starter project does not
implement this feature yet.

## Definitions

`same slot` means the same `room_id`, `start_time`, and `end_time`.

`overlap` still uses the existing booking overlap rule:

```text
start_a < end_b and start_b < end_a
```

Only confirmed bookings block a requested slot. Cancelled bookings do not block.
Waitlisted bookings do not block additional waitlisted requests.

## Expected Behavior

| Scenario | Expected result |
| --- | --- |
| first booking for empty slot | `201 Created` with `status: confirmed` |
| second booking for same room and same slot | `201 Created` with `status: waitlisted` |
| third booking for same room and same slot | `201 Created` with `status: waitlisted`; request order is preserved |
| adjacent booking | `201 Created` with `status: confirmed` |
| same time in different room | `201 Created` with `status: confirmed` |
| cancel confirmed booking with no waitlist | cancelled booking becomes `cancelled`; no promotion occurs |
| cancel confirmed booking with waitlist | cancelled booking becomes `cancelled`; earliest waitlisted booking for the same slot becomes `confirmed` |
| cancel waitlisted booking | only that booking becomes `cancelled`; no promotion occurs |

## API Response Rule

`DELETE /bookings/{booking_id}` should return the booking that was cancelled.

If promotion occurs, clients can observe the promoted booking through
`GET /bookings`.

## Ordering Rule

Waitlist order is request order. In this starter project, request order can be
represented by ascending booking `id`.

## Non-goals

- No authentication.
- No notifications.
- No recurring bookings.
- No external calendar integration.
- No endpoint rename.
- No dependency changes.
