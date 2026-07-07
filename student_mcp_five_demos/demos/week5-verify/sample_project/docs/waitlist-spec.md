# Waitlist Status Helper Spec

The waitlist helper is a small Python module for admissions staff who need a
simple way to track student waitlist status.

## Data Rules

- Each student is keyed by normalized email address.
- Email normalization trims leading and trailing spaces and lowercases the
  address.
- Display names are stored without leading or trailing spaces.
- Blank email addresses are rejected.
- Blank display names are rejected.

## Status Rules

Allowed statuses:

- `waiting`
- `admitted`
- `declined`

New students start with `waiting` status. Status updates normalize both the
student email lookup and the submitted status text. Unknown statuses are
rejected.

## Summary Rule

The summary reports counts for all three statuses, including zero counts:

```python
{"admitted": 0, "declined": 0, "waiting": 0}
```

## Readiness Definition

The project is ready when:

- the implementation satisfies `task-contract.yaml`;
- the behavior matches this spec;
- `bash scripts/verify.sh` exits with status code 0;
- the verification output reports all 15 tests passing.
