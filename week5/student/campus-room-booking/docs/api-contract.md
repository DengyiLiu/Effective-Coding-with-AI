# API Contract

This document describes the starter API behavior before the Week 5 feature is
implemented.

## Rooms

### GET /rooms

Returns the seeded campus rooms.

Example response:

```json
[
  {
    "id": "study-a",
    "name": "Study Room A",
    "room_type": "study",
    "capacity": 4
  }
]
```

## Bookings

### GET /bookings

Returns booking records in id order.

Booking statuses in the starter:

```text
confirmed
cancelled
```

The Week 5 feature may add:

```text
waitlisted
```

### POST /bookings

Creates a confirmed booking when the requested room and time slot are available.

Request body:

```json
{
  "requester": "Alice",
  "room_id": "study-a",
  "start_time": "2026-07-01T10:00:00Z",
  "end_time": "2026-07-01T11:00:00Z"
}
```

Success response:

```http
201 Created
```

```json
{
  "id": 1,
  "room_id": "study-a",
  "requester": "Alice",
  "start_time": "2026-07-01T10:00:00Z",
  "end_time": "2026-07-01T11:00:00Z",
  "status": "confirmed",
  "created_at": "2026-07-01T14:00:00Z"
}
```

Starter conflict behavior:

```http
409 Conflict
```

```json
{
  "detail": "room is already booked for that time slot"
}
```

Week 5 feature target:

```text
An overlapping request for the same room/time should create a waitlisted
booking instead of returning 409.
```

### DELETE /bookings/{booking_id}

Cancels an existing confirmed booking.

Success response:

```http
200 OK
```

```json
{
  "id": 1,
  "room_id": "study-a",
  "requester": "Alice",
  "start_time": "2026-07-01T10:00:00Z",
  "end_time": "2026-07-01T11:00:00Z",
  "status": "cancelled",
  "created_at": "2026-07-01T14:00:00Z"
}
```

Week 5 feature target:

```text
If a confirmed booking is cancelled and a waitlist exists for the same room and
time slot, the earliest waitlisted booking should be promoted to confirmed.
```

## Error Responses

Unknown room:

```http
404 Not Found
```

Invalid time range:

```http
400 Bad Request
```

Overlapping booking in starter:

```http
409 Conflict
```

Already cancelled booking:

```http
409 Conflict
```
