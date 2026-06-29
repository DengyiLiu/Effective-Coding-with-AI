# Decision Log

## Accepted AI Suggestions

| Suggestion | Why accepted |
| --- | --- |
| Add `waitlisted` as a booking status | Minimal data model change needed for the feature |
| Keep endpoint names unchanged | Matches approval scope and preserves API ergonomics |
| Add focused waitlist tests | Directly maps feature behavior to evidence |

## Modified AI Suggestions

| Original suggestion | Final decision | Why |
| --- | --- | --- |
| Remove the old overlap regression | Update it instead | The old test should not be deleted; it should assert the approved new waitlist behavior |

## Rejected AI Suggestions

| Suggestion | Why rejected |
| --- | --- |
| Add email notifications | Non-goal |
| Modify `scripts/verify.sh` | Verification script changes require separate approval and were unnecessary |

## Deferred Suggestions

| Suggestion | Follow-up reason |
| --- | --- |
| Remove unused `BookingConflictError` cleanup | Could distract from the feature and is better as a separate refactor |

## Most Important Human Decision

The most important human decision in this workflow was:

```text
Approving a narrow scope that allowed the old conflict behavior tests to be
updated only to the new waitlist contract, while forbidding verification script
changes, dependency changes, and unrelated endpoint changes.
```
