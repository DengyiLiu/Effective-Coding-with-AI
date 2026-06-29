# AIM 5012 Week 5 Instructor Guide

Topic: AI Coding Workflow on a Real Project.

Project: Campus Room Booking API.

Feature: Waitlist + Cancellation Promotion.

## Instructor Goal

Students should leave Week 5 able to execute a controlled AI coding workflow:

```text
contract -> context -> reconnaissance -> plan -> approval -> implementation
-> verification -> repair -> review -> decision log
```

Keep returning the class to three questions:

```text
What did the workflow prevent?
What evidence proves the work?
Where did the human make a decision?
```

## Before Class

Prepare:

- A working `campus-room-booking` starter folder.
- Baseline tests passing with `bash scripts/verify.sh`.
- Student artifact templates from `student/artifact-templates/`.
- A slide deck generated from `AIM5012_Week5_Slide_Blueprint.md`.

Verify:

```bash
cd campus-room-booking
bash scripts/verify.sh
```

The first classroom message should be:

```text
The project is already working.
The goal is not to rewrite it.
The goal is to add one feature safely.
```

## Session 5.1: Designing the Workflow Before Coding

### 0-8 min - Why the old way fails

Show the bad prompt:

```text
Add waitlist support to this booking API.
```

Ask students to predict likely AI failures.

Expected answers:

- rewrite the booking service
- change endpoint names
- remove old conflict behavior without documenting it
- forget cancellation promotion
- add unnecessary dependencies
- update tests only for happy path
- claim the feature works without running tests

Instructor line:

```text
The problem is not only prompting. The problem is missing workflow.
```

### 8-18 min - Project walkthrough

Open these files:

```text
app/main.py
app/models.py
app/booking_service.py
tests/
scripts/verify.sh
docs/api-contract.md
```

Run:

```bash
bash scripts/verify.sh
```

Do not explain every FastAPI detail. Focus on existing behavior and testable
contracts.

### 18-30 min - Feature walkthrough

Use this story:

```text
Alice books Room A, 10:00-11:00 -> confirmed
Bob books Room A, 10:00-11:00 -> waitlisted
Carla books Room A, 10:00-11:00 -> waitlisted behind Bob
Alice cancels -> Bob becomes confirmed, Carla remains waitlisted
```

Ask:

```text
What can go wrong?
```

Push students toward:

- state transition mistakes
- ordering mistakes
- cancellation edge cases
- accidental API contract changes
- weak tests
- scope creep

### 30-42 min - Skill, workflow, agent, harness

Define:

```text
Skill = one bounded capability.
Workflow = ordered skills and gates.
Agent = model-driven action selection.
Harness = controls, tools, logs, verification, recovery.
```

Bridge:

```text
Week 5 is manual workflow. Week 6 starts turning the workflow into a harness.
```

### 42-58 min - Task contract workshop

Have students create:

```text
runs/week5-run-001/task-contract.yaml
```

Use the template:

```text
student/artifact-templates/task-contract.yaml
```

Checkpoint questions:

- Are acceptance criteria testable?
- Are non-goals explicit?
- Which public API changes need approval?
- What command proves the work?

### 58-70 min - Workflow spec

Have students create:

```text
runs/week5-run-001/workflow-spec.yaml
```

Use the template:

```text
student/artifact-templates/workflow-spec.yaml
```

Emphasize:

```text
The workflow spec is the operating system for the AI coding task.
```

### 70-82 min - Context packet and skill contracts

Have students create:

```text
runs/week5-run-001/context-packet.md
runs/week5-run-001/skill-contracts.yaml
```

Use:

```text
student/artifact-templates/context-packet.md
student/artifact-templates/skill-contracts.yaml
```

Main teaching point:

```text
Context should be staged, not dumped.
Skills should have boundaries, not just instructions.
```

### 82-90 min - Exit ticket

Ask students to answer:

```text
1. What is the highest-risk part of this feature?
2. Which file should AI inspect first?
3. What change should require human approval?
```

Collect answers quickly or have students paste them at the bottom of their
workflow folder notes.

## Session 5.2: Executing, Verifying, Reviewing

### 0-10 min - Recap

Write on board:

```text
Task Contract -> Workflow Spec -> Context Packet -> Reconnaissance -> Plan
-> Human Gate -> Implementation -> Verification -> Review -> Decision Log
```

Instructor line:

```text
Today, the goal is not just to make tests pass. The goal is to produce a
trustworthy workflow run.
```

### 10-25 min - AI reconnaissance

Prompt students to use:

```text
You are executing the repo_reconnaissance skill.

Read:
- runs/week5-run-001/task-contract.yaml
- runs/week5-run-001/context-packet.md
- docs/api-contract.md
- docs/architecture.md
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

Save:

```text
runs/week5-run-001/reconnaissance.md
```

Instructor checks:

- Did AI identify the service layer?
- Did AI understand current conflict behavior?
- Did AI identify cancellation logic?
- Did AI avoid implementation too early?

### 25-38 min - Implementation plan

Prompt students to use:

```text
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

Return a plan suitable for human approval.
```

Save:

```text
runs/week5-run-001/implementation-plan.md
```

Reject vague plans. A usable plan names files, tests, acceptance criteria, and
non-goals.

### 38-48 min - Human approval gate

Have students write:

```text
runs/week5-run-001/approval.md
```

Use:

```text
student/artifact-templates/approval.md
```

Students should approve file scope explicitly.

### 48-62 min - Controlled implementation

Prompt students to use:

```text
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
- Existing conflict-rejection tests may be updated only to assert the approved waitlist behavior.
- Preserve backward-compatible behavior.
- Add tests for acceptance criteria.

After implementation, report:
1. changed files
2. what changed
3. which acceptance criteria are covered
4. verification command to run
```

Save the diff:

```bash
git diff > runs/week5-run-001/diff.patch
```

If a student does not use git, have them create `change-summary.md`, but prefer
`diff.patch`.

### 62-72 min - Verification report

Run:

```bash
bash scripts/verify.sh
```

Save:

```text
runs/week5-run-001/verification-report.md
```

Use:

```text
student/artifact-templates/verification-report.md
```

Do not accept "tests passed" as enough. Students must map evidence to each
acceptance criterion.

### 72-80 min - Repair loop

If verification fails, require analysis before edits:

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

Policy:

```text
Maximum two repair attempts, then NEEDS_HUMAN.
```

### 80-88 min - Fresh-context review and decision log

Students should open a fresh AI context and provide only:

```text
task-contract.yaml
implementation-plan.md
approval.md
diff.patch
verification-report.md
```

Review prompt:

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
runs/week5-run-001/decision-log.md
```

Use:

```text
student/artifact-templates/decision-log.md
```

### 88-90 min - Week 6 bridge

Close with:

```text
This week, you executed the workflow manually.
Next week, we start turning the workflow into a harness.
```

## Common Instructor Interventions

If students ask AI to implement too early:

```text
Stop. Which artifact gave permission to edit code?
```

If AI proposes changing endpoints:

```text
Is that in the approved file scope? Is it in needs_approval?
```

If tests pass but evidence is weak:

```text
Which acceptance criterion proves FIFO promotion?
```

If students want to modify `scripts/verify.sh`:

```text
That requires explicit approval. Why is the verifier wrong rather than the code?
```

If AI gives a broad refactor:

```text
Ask for the smallest implementation that satisfies the task contract.
```

## Grading Focus

Grade the workflow trail, not only the final code.

High-scoring submissions show:

- clear scope
- correct reconnaissance
- minimal plan
- real approval gate
- tests mapped to acceptance criteria
- verification output
- fresh-context review
- human decision log
- honest retrospective
