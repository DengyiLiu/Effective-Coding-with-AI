# Workflow Retrospective

## What worked well?

The workflow forced reconnaissance before implementation. The implementation
stayed in the service layer and tests instead of spreading across unrelated
routes or dependencies.

## Where did AI help most?

Mapping acceptance criteria to concrete tests and identifying cancellation
promotion edge cases.

## Where did AI create risk?

It could easily treat the old conflict rejection test as obsolete and delete it.
The approval gate reframed that test as a contract update rather than a removal.

## Which workflow stage prevented the biggest mistake?

The human approval gate. It explicitly allowed updating conflict tests only for
the approved behavior change and blocked changes to `scripts/verify.sh`.

## Which artifact was weakest?

The context packet. It listed important files, but a stronger packet would call
out the exact old `409 Conflict` regression before planning.

## What should be automated in Week 6?

Creating the run folder, copying templates, running verification, collecting
diffs, and checking that acceptance criteria have evidence.

## What should remain human-controlled?

Approval of public API changes, acceptance or rejection of review findings, and
decisions about scope expansion.

## What would you change before running this workflow again?

Add a small pre-flight checklist that asks whether old tests should be preserved,
updated, or treated as regression blockers.
