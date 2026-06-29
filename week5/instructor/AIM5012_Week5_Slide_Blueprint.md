# AIM 5012 Week 5 Slide Blueprint

This is a blueprint for a later deck. Slides should be primarily in English.
Instructor explanation can be bilingual.

## Part 1 - Framing the Week

### Slide 1 - Week 5: AI Coding Workflow on a Real Project

Bullets:

- Campus Room Booking API
- Feature: Waitlist + Cancellation Promotion
- From prompt-driven coding to controlled workflow

Purpose: Establish that Week 5 is no longer a toy prompt exercise.

### Slide 2 - From Prompting to Workflow

Text:

```text
Good AI coding is not "prompt -> code."
Good AI coding is "contract -> plan -> approval -> implementation -> verification -> review."
```

Purpose: Introduce the central shift.

### Slide 3 - What We Are Building Today

Bullets:

- Existing room booking API
- Add waitlist behavior
- Add automatic promotion after cancellation
- Preserve existing behavior

Purpose: Introduce the project and feature.

### Slide 4 - Why This Project Is Realistic

Bullets:

- Existing behavior
- State changes
- Edge cases
- Backward compatibility
- Tests
- Review

Purpose: Explain why this is more realistic than a single-script task.

### Slide 5 - The Core Question

Text:

```text
How do we let AI change existing software without losing control?
```

Purpose: Frame the rest of the week.

## Part 2 - Project Understanding

### Slide 6 - Existing System

Bullets:

- Rooms
- Bookings
- Conflict detection
- Cancellation
- Tests
- Verification script

Purpose: Show the starter is already working.

### Slide 7 - Baseline Flow

Text:

```text
Request booking
-> check room exists
-> check time slot
-> check overlap
-> create confirmed booking or reject
```

Purpose: Help students understand current logic.

### Slide 8 - New Feature Flow

Text:

```text
Available slot -> confirmed
Occupied slot -> waitlisted
Cancel confirmed booking -> promote earliest waitlisted request
```

Purpose: Make the feature concrete.

### Slide 9 - State Transition Diagram

Text:

```text
requested -> confirmed -> cancelled
requested -> waitlisted -> confirmed -> cancelled
waitlisted -> cancelled
```

Purpose: Show that this is a state transition problem.

### Slide 10 - What Can Go Wrong?

Bullets:

- Wrong promotion order
- Broken cancellation
- Changed endpoint contract
- Weak tests
- Unrelated refactor
- Hidden scope creep

Purpose: Create the need for workflow.

## Part 3 - Workflow Concepts

### Slide 11 - Skill vs Workflow vs Agent vs Harness

Text:

```text
Skill = one bounded capability
Workflow = ordered skills and gates
Agent = model-driven action selection
Harness = controls, tools, logs, verification, recovery
```

Purpose: Define the conceptual chain from Week 5 to Week 6.

### Slide 12 - Why We Start with Workflow

Bullets:

- Well-defined task
- Predictable steps
- Human gates
- Deterministic verification
- Lower risk than full autonomy

Purpose: Explain why the course starts with manual workflow.

### Slide 13 - The Week 5 Workflow

Text:

```text
Task Contract
-> Context Packet
-> Reconnaissance
-> Plan
-> Approval
-> Implementation
-> Verification
-> Repair
-> Review
-> Decision Log
```

Purpose: Show the full path.

### Slide 14 - The Rule of the Week

Text:

```text
No code before reconnaissance.
No implementation before approval.
No completion without verification.
No acceptance without human judgment.
```

Purpose: Give students a memorable rule.

## Part 4 - Task Contract

### Slide 15 - Artifact: task-contract.yaml

Text:

```text
Defines done, not done, allowed, forbidden, and verification.
```

Purpose: Introduce the first artifact.

### Slide 16 - Product Request

Text:

```text
When a requested room/time slot is already booked,
store the request as waitlisted.

When the confirmed booking is cancelled,
promote the earliest waitlisted booking.
```

Purpose: Start from natural language.

### Slide 17 - Acceptance Criteria

Bullets:

- Confirmed booking
- Waitlisted booking
- FIFO promotion
- Cancel with no waitlist
- Cancel waitlisted request
- Backward compatibility
- Tests

Purpose: Convert request into testable outcomes.

### Slide 18 - Non-goals

Bullets:

- No authentication
- No frontend
- No calendar integration
- No notifications
- No recurring bookings
- No unrelated redesign

Purpose: Prevent scope creep.

### Slide 19 - Constraints

Bullets:

- Allowed
- Needs approval
- Forbidden

Purpose: Teach permission boundaries.

## Part 5 - Workflow Spec and Skill Contracts

### Slide 20 - Artifact: workflow-spec.yaml

Text:

```text
A workflow spec defines stages, actors, permissions, gates, and failure handling.
```

Purpose: Show workflow as an executable structure.

### Slide 21 - Workflow States

Bullets:

- NEW
- SCOPED
- CONTEXT_READY
- PLAN_READY
- APPROVED
- IMPLEMENTING
- VERIFYING
- REPAIRING
- REVIEWING
- DONE
- NEEDS_HUMAN

Purpose: Preview the Week 6 state machine.

### Slide 22 - Code Edit Permissions

Bullets:

- Reconnaissance: no edits
- Planning: no edits
- Approval: no edits
- Implementation: approved files only
- Verification: no edits
- Review: no edits

Purpose: Emphasize permission control.

### Slide 23 - Artifact: skill-contracts.yaml

Text:

```text
Each skill needs:
purpose
inputs
outputs
allowed actions
forbidden actions
success criteria
failure policy
```

Purpose: Treat skills as workflow nodes.

### Slide 24 - Artifact: context-packet.md

Text:

```text
Context should be staged, relevant, and task-specific.
```

Purpose: Stop students from dumping the whole repo into AI without structure.

## Part 6 - Running the Workflow

### Slide 25 - Stage 1: Reconnaissance

Text:

```text
AI reads before it writes.
```

Purpose: Train students to inspect before editing.

### Slide 26 - Reconnaissance Output

Bullets:

- Relevant files
- Current flow
- Existing tests
- Risks
- Minimal edit scope
- Open questions

Purpose: Define the expected output.

### Slide 27 - Stage 2: Implementation Plan

Text:

```text
A plan must map each acceptance criterion to code and tests.
```

Purpose: Prevent vague planning.

### Slide 28 - Plan Review Checklist

Bullets:

- Is the scope minimal?
- Are all acceptance criteria covered?
- Are tests specific?
- Are non-goals protected?
- Are risky changes flagged?

Purpose: Teach students how to review a plan.

### Slide 29 - Stage 3: Human Approval

Text:

```text
The human gate turns a plan into permission.
```

Purpose: Make approval meaningful.

### Slide 30 - Approved File Scope

Text:

```text
AI may modify:
service
models
schemas
tests

AI may not modify:
verification script
dependencies
unrelated endpoints
unrelated tests
```

Purpose: Show concrete scope control.

### Slide 31 - Stage 4: Implementation

Text:

```text
Implement only the approved plan.
Stay inside the approved file scope.
Do not weaken tests.
```

Purpose: Move into code while preserving constraints.

### Slide 32 - Stage 5: Verification

Text:

```text
Run the command.
Paste the output.
Map evidence to acceptance criteria.
```

Purpose: Turn tests into evidence.

### Slide 33 - Stage 6: Repair Loop

Text:

```text
Analyze before fixing.
Smallest fix only.
Maximum two attempts.
Escalate to human.
```

Purpose: Prevent uncontrolled repair loops.

### Slide 34 - Stage 7: Fresh-context Review

Text:

```text
A reviewer should see the task, plan, diff, and evidence,
not the whole chat history.
```

Purpose: Teach independent review.

### Slide 35 - Review Categories

Bullets:

- Blocking
- Should fix
- Optional
- Questions

Purpose: Structure review output.

### Slide 36 - Stage 8: Decision Log

Text:

```text
AI suggests.
Human decides.
The decision must be recorded.
```

Purpose: Reinforce human judgment.

## Part 7 - Reflection and Assessment

### Slide 37 - What Counts as Done?

Bullets:

- Feature works
- Tests pass
- Acceptance criteria have evidence
- No blocking review findings
- Human decision recorded

Purpose: Define done.

### Slide 38 - Common Workflow Failures

Bullets:

- Spec failure
- Context failure
- Planning failure
- Permission failure
- Implementation failure
- Verification failure
- Review failure
- Human oversight failure

Purpose: Help students diagnose process failures.

### Slide 39 - Assignment

Text:

```text
Submit a complete workflow run folder.
```

Purpose: Introduce the assignment.

### Slide 40 - Rubric

Bullets:

- Task contract
- Workflow spec
- Reconnaissance
- Plan and approval
- Verification
- Review
- Decision log
- Retrospective

Purpose: Explain grading priorities.

### Slide 41 - Bridge to Week 6

Text:

```text
Manual workflow -> automated harness
```

Purpose: Connect to next week.

### Slide 42 - Final Takeaway

Text:

```text
The goal is not to make AI write more code.
The goal is to make AI coding controllable, verifiable, and reviewable.
```

Purpose: Close with the main lesson.
