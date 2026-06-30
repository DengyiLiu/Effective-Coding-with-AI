# AIM 5012 Week 5 Live Workflow Demo Guide

Use this guide to run a live instructor demo from the student starter project.
The goal is to show the workflow, not to teach FastAPI.

## Demo Goal

By the end of the demo, the API should support this behavior:

```text
Alice books a room -> confirmed
Bob books the same room/time -> waitlisted
Carla books the same room/time -> waitlisted
Alice cancels -> Bob becomes confirmed, Carla remains waitlisted
```

Main teaching point:

```text
AI coding is controlled by workflow, not by one big prompt.
```

## 0. Create A Live Demo Copy

Do not edit the original starter folder directly.

```bash
cd /Users/liudengyi/Documents/adjunct/summer2026/week5/student
cp -R campus-room-booking campus-room-booking-live-demo
cd campus-room-booking-live-demo
```

Initialize git so you can capture a diff later:

```bash
git init
git add .
git commit -m "Baseline starter"
```

Install dependencies and run baseline verification:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
```

Expected result:

```text
15 passed
```

Say:

```text
The starter already works. Our job is not to rewrite it.
Our job is to change it safely.
```

## 1. Show The Starter Behavior

Start the API without reload:

```bash
python -m uvicorn app.main:app --port 8001
```

Open:

```text
http://127.0.0.1:8001/docs
```

In Swagger, create Alice with `POST /bookings`:

```json
{
  "requester": "Alice",
  "room_id": "study-a",
  "start_time": "2026-07-01T10:00:00Z",
  "end_time": "2026-07-01T11:00:00Z"
}
```

Point out:

```text
Alice -> confirmed
```

Create Bob with the same room and time:

```json
{
  "requester": "Bob",
  "room_id": "study-a",
  "start_time": "2026-07-01T10:00:00Z",
  "end_time": "2026-07-01T11:00:00Z"
}
```

Point out:

```text
Current starter behavior: conflict -> 409 Conflict
```

Say:

```text
Today we will change conflict -> reject into conflict -> waitlist.
But we will not ask AI to jump straight into code.
```

Stop the server:

```text
CTRL+C
```

## 2. Create The Workflow Run Folder

```bash
mkdir -p runs/week5-run-001
cp ../artifact-templates/* runs/week5-run-001/
find runs/week5-run-001 -maxdepth 1 -type f | sort
```

Say:

```text
This folder is our local PR trail.
Every AI step must leave evidence here.
```

## 3. Show The Task Contract

Open:

```text
runs/week5-run-001/task-contract.yaml
```

Only explain four parts:

```text
acceptance_criteria = what must work
non_goals = what we will not build
constraints = what AI can and cannot change
verification = how we prove the work
```

Say:

```text
A task contract turns a vague request into something testable.
```

## 4. Show The Bad Prompt

Show this prompt but do not use it to edit code:

```text
Add waitlist support to this FastAPI app.
```

Ask:

```text
What could go wrong?
```

Expected answers:

```text
- AI changes endpoint names
- AI adds dependencies
- AI deletes or weakens tests
- AI modifies scripts/verify.sh
- AI implements waitlisting but forgets promotion
- AI rewrites too much of the app
```

Say:

```text
The problem is not only prompting. The problem is missing workflow.
```

## 5. AI Reconnaissance

Give AI this prompt:

```text
You are executing the repo_reconnaissance skill.

Read:
- runs/week5-run-001/task-contract.yaml
- runs/week5-run-001/context-packet.md
- docs/api-contract.md
- docs/architecture.md
- docs/waitlist-spec.md
- AGENTS.md
- project files

Rules:
- Do not edit code.
- Do not propose implementation yet.
- Do not add dependencies.
- Only inspect and summarize.

Return:
1. relevant files
2. current booking flow
3. current cancellation flow
4. current overlap/conflict logic
5. existing tests
6. verification command
7. likely risks
8. minimal edit scope
9. questions before implementation
```

Save the response:

```text
runs/week5-run-001/reconnaissance.md
```

Say:

```text
First control: AI must read before it writes.
```

Check that AI identified:

```text
app/booking_service.py
app/models.py
tests/
docs/waitlist-spec.md
current conflict behavior: 409
```

## 6. Implementation Plan

Give AI this prompt:

  You are executing the implementation_planner skill for Week 5.

  Use these files:
  - runs/week5-run-001/task-contract.yaml
  - runs/week5-run-001/context-packet.md
  - runs/week5-run-001/reconnaissance.md
  - docs/api-contract.md
  - docs/waitlist-spec.md
  - AGENTS.md

  Important answers to open questions:
  - Any valid same-room overlap with a confirmed booking should create a waitlisted booking.
  - Cancellation promotion is limited to the exact same slot: same room_id, same start_time, same end_time.
  - The old create-booking 409 conflict behavior should be replaced for valid overlaps.
  - Other 409 behavior, such as cancelling an already-cancelled booking, should remain.

  Rules:
  - Do not edit any files.
  - Do not write implementation code.
  - Keep the plan minimal.
  - Do not add dependencies.
  - Do not change endpoint names.
  - Do not modify scripts/verify.sh.
  - Do not delete or weaken tests.
  - If existing tests need to change because the product behavior changed, explain why.
  - Map every acceptance criterion to implementation and test evidence.

  Return a Markdown implementation plan with these sections:
  1. Goal
  2. Proposed files to modify
  3. Files not to modify
  4. Data model changes
  5. Booking creation behavior changes
  6. Cancellation promotion behavior changes
  7. Test plan
  8. Acceptance criteria mapping
  9. Risks and mitigations
  10. Approval checklist

  store the markdown as runs/week5-run-001/implementation-plan.md

<!-- ```text
You are executing the implementation_planner skill.

Use:
- task-contract.yaml
- reconnaissance.md
- context-packet.md

Rules:
- Do not edit code.
- Keep the plan minimal.
- Map every acceptance criterion to implementation and test evidence.
- List every file you propose to modify.
- Explain why each file must change.
- State what you will not change.

Return a plan suitable for human approval. -->
```

Save the response:

```text
runs/week5-run-001/implementation-plan.md
```

Good proposed scope:

```text
app/models.py
app/booking_service.py
tests/test_booking_create.py
tests/test_existing_behavior.py
tests/test_waitlist.py
docs/api-contract.md
```

Reject or question:

```text
requirements.txt
scripts/verify.sh
endpoint names
unrelated routes
```

Say:

```text
A plan is not permission. It must pass the human gate first.
```

## 7. Human Approval Gate

Open:

```text
runs/week5-run-001/approval.md
```

Make sure the approved scope says:

```text
AI may not modify scripts/verify.sh.
AI may not add dependencies.
AI may not change endpoint names.
AI may not delete or weaken tests.
AI may update old conflict tests only to match the approved waitlist behavior.
```

Say:

```text
Approval is not a formality.
This is where the human turns a plan into permission.
```

## 8. Controlled Implementation

Give AI this prompt:

  You are executing the controlled implementation stage for Week 5.

  Use these files:
  - runs/week5-run-001/task-contract.yaml
  - runs/week5-run-001/reconnaissance.md
  - runs/week5-run-001/implementation-plan.md
  - runs/week5-run-001/approval.md
  - docs/api-contract.md
  - docs/waitlist-spec.md
  - AGENTS.md

  Rules:
  - Implement only the approved plan.
  - Stay inside the approved file scope.
  - Do not modify `scripts/verify.sh`.
  - Do not modify `requirements.txt`.
  - Do not change endpoint names.
  - Do not add dependencies.
  - Do not delete existing tests.
  - Do not weaken assertions.
  - Update old conflict tests only where product behavior intentionally changed from 409 rejection to waitlist creation.
  - Add tests for waitlist creation, FIFO order, cancellation promotion, no-waitlist cancellation, and waitlisted cancellation.
  - Preserve existing room listing behavior.
  - Preserve cancellation 404 and already-cancelled 409 behavior.

  Important product decisions:
  - Any valid same-room overlap with a confirmed booking should create a waitlisted booking.
  - Promotion is limited to the exact same slot: same `room_id`, same `start_time`, same `end_time`.
  - Cancelling a waitlisted booking should only cancel that waitlisted booking and should not promote anyone.
  - Cancelling a confirmed booking should promote the earliest waitlisted booking for the exact same slot, if one exists.
  - Adjacent bookings should remain confirmed.
  - Same-time bookings in different rooms should remain confirmed.

  After implementation, report:
  1. Changed files
  2. Summary of behavior changes
  3. Tests added or updated
  4. Acceptance criteria covered
  5. Verification command to run

<!-- ```text
You are executing the implementation stage.

Use:
- task-contract.yaml
- implementation-plan.md
- approval.md

Rules:
- Implement only the approved plan.
- Stay within approved file scope.
- Do not add dependencies.
- Do not change endpoint names.
- Do not modify scripts/verify.sh.
- Do not delete or weaken existing tests.
- You may update existing conflict-rejection tests only to match the approved waitlist behavior.
- Preserve backward-compatible behavior.
- Add tests for acceptance criteria.

After implementation, report:
1. changed files
2. what changed
3. which acceptance criteria are covered
4. verification command to run
``` -->

After AI edits the project, capture the diff:

```bash
git diff > runs/week5-run-001/diff.patch
```

Say:

```text
The diff is the review object. We do not review vague chat history.
```

## 9. Verification

Run:

```bash
bash scripts/verify.sh
```

If it passes, fill:

```text
runs/week5-run-001/verification-report.md
```

The report must map tests to acceptance criteria.

If it fails, do not say "fix it." Use this repair prompt:

```text
The verification command failed.

Before editing anything, analyze:
1. What failed?
2. Is this an implementation issue, test issue, environment issue, or task contract issue?
3. What is the smallest fix?
4. Which files need to change?
5. Are you proposing to modify tests? If yes, explain why that is valid under the task contract.

Rules:
- Do not weaken tests.
- Do not skip tests.
- Do not change scripts/verify.sh.
- Do not expand scope.
- Do not add dependencies.
- Do not change endpoint names without approval.
```

Say:

```text
Repair is controlled. It is not an unlimited fix-it loop.
```

## 10. Show The Final Behavior

Start the API again:

```bash
python -m uvicorn app.main:app --port 8001
```

Open:

```text
http://127.0.0.1:8001/docs
```

Create Alice:

```text
Alice -> confirmed
```

Create Bob for the same room/time:

```text
Bob -> waitlisted
```

Create Carla for the same room/time:

```text
Carla -> waitlisted
```

Run `GET /bookings`.

Expected state:

```text
Alice -> confirmed
Bob -> waitlisted
Carla -> waitlisted
```

Run `DELETE /bookings/1`.

Then run `GET /bookings` again.

Expected state:

```text
Alice -> cancelled
Bob -> confirmed
Carla -> waitlisted
```

Say:

```text
This is the feature. But we only accept it because verification and review support it.
```

## 11. Fresh-context Review

Open a fresh AI context. Provide only:

```text
task-contract.yaml
implementation-plan.md
approval.md
diff.patch
verification-report.md
```

Prompt:

```text
You are executing the reviewer skill from a fresh context.

You receive only:
- task contract
- approved plan
- approval notes
- diff patch
- verification report

Do not rewrite the code.

Review for:
1. missed acceptance criteria
2. unnecessary changes
3. weak or missing tests
4. possible regressions
5. deviations from the approved plan
6. signs that tests were weakened
7. reliability risks

Return findings grouped as:
- Blocking
- Should fix
- Optional
- Questions for the author
```

Save:

```text
runs/week5-run-001/ai-review.md
```

Then fill:

```text
runs/week5-run-001/decision-log.md
```

Say:

```text
AI can review. Humans decide.
```

## 12. Closing

Repeat the four rules:

```text
No code before reconnaissance.
No implementation before approval.
No completion without verification.
No acceptance without human judgment.
```

Bridge to Week 6:

```text
This week we executed the workflow manually.
Next week we start turning this workflow into a harness.
```
