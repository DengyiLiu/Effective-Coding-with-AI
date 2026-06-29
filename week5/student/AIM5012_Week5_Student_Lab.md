# AIM 5012 Week 5 Student Lab

## Title

Local AI Coding Workflow Run on a Real Project.

## Project

```text
Campus Room Booking API
Feature: Waitlist + Cancellation Promotion
```

## Concept Framework

Week 5 is not about writing a better one-shot prompt. It is about controlling
AI coding work through a workflow.

| Concept | Meaning in Week 5 |
| --- | --- |
| Prompt | A single instruction given to AI |
| Skill | A bounded capability such as reconnaissance, planning, implementation, verification, or review |
| Workflow | An ordered process with stages, artifacts, permissions, gates, and repair policy |
| Harness | The control system around AI work: tests, scripts, templates, diffs, review, and evidence |

## Core Rule

You must not directly ask AI to implement the feature.

You must execute the workflow:

```text
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision
```

## Opening Demo: Bad Prompt vs Workflow Prompt

Bad prompt:

```text
Add waitlist support to this FastAPI app.
```

Before coding, identify what could go wrong:

- AI changes endpoint names.
- AI adds unnecessary dependencies.
- AI deletes or weakens tests.
- AI modifies `scripts/verify.sh`.
- AI implements waitlisting but forgets cancellation promotion.
- AI rewrites storage or routing instead of making a small service-layer change.

Workflow prompt:

```text
You are executing the repo_reconnaissance skill.
Do not edit code.
Read the task contract, context packet, docs, tests, and relevant project files.
Return current behavior, relevant files, risks, and minimal edit scope.
```

The goal is to slow the work down enough that it becomes controllable.

## What You Are Building

The starter API already supports:

```text
- list rooms
- create confirmed bookings
- reject overlapping bookings
- cancel bookings
- list bookings
- run existing tests
```

Your feature:

```text
If a room/time slot is already booked, create a waitlisted booking.
When the confirmed booking is cancelled, promote the earliest waitlisted booking.
```

Read the detailed behavior rules before planning:

```text
docs/waitlist-spec.md
```

## Required Run Folder

Create:

```text
runs/week5-run-001/
```

Your final folder must contain:

```text
runs/week5-run-001/
├── task-contract.yaml
├── workflow-spec.yaml
├── skill-contracts.yaml
├── context-packet.md
├── reconnaissance.md
├── implementation-plan.md
├── approval.md
├── diff.patch
├── verification-report.md
├── ai-review.md
├── decision-log.md
└── retrospective.md
```

Templates are in:

```text
student/artifact-templates/
```

## Stage 0: Baseline Verification

Before asking AI to do anything, run:

```bash
bash scripts/verify.sh
```

Record the result in your notes. The project should already pass.

Also read:

- `docs/api-contract.md`
- `docs/architecture.md`
- `docs/waitlist-spec.md`
- `AGENTS.md`

## Stage 1: Task Contract

Create:

```text
runs/week5-run-001/task-contract.yaml
```

Use:

```text
student/artifact-templates/task-contract.yaml
```

Your task contract must include:

- problem
- user story
- acceptance criteria
- non-goals
- constraints
- verification command
- evidence required

## Stage 2: Workflow Spec

Create:

```text
runs/week5-run-001/workflow-spec.yaml
```

Use:

```text
student/artifact-templates/workflow-spec.yaml
```

Your workflow spec must define:

- states
- stages
- actors
- code edit permissions
- human gates
- repair policy
- done condition

## Stage 3: Context Packet and Skill Contracts

Create:

```text
runs/week5-run-001/context-packet.md
runs/week5-run-001/skill-contracts.yaml
```

Use:

```text
student/artifact-templates/context-packet.md
student/artifact-templates/skill-contracts.yaml
```

## Stage 4: AI Reconnaissance

Prompt:

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

## Stage 5: Implementation Plan

Prompt:

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

## Stage 6: Human Approval

Create:

```text
runs/week5-run-001/approval.md
```

Use:

```text
student/artifact-templates/approval.md
```

You must explicitly approve file scope before implementation.

## Stage 7: Controlled Implementation

Prompt:

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
- You may update existing conflict-rejection tests only to match the approved waitlist behavior.
- Preserve backward-compatible behavior.
- Add tests for acceptance criteria.

After implementation, report:
1. changed files
2. what changed
3. which acceptance criteria are covered
4. verification command to run
```

After implementation, save:

```bash
git diff > runs/week5-run-001/diff.patch
```

If your project is not using git, create:

```text
runs/week5-run-001/change-summary.md
```

## Stage 8: Verification

Run:

```bash
bash scripts/verify.sh
```

Create:

```text
runs/week5-run-001/verification-report.md
```

Use:

```text
student/artifact-templates/verification-report.md
```

Your report must include:

- command output
- pass/fail result
- acceptance criteria mapping
- failures encountered
- fixes made
- remaining limitations

## Stage 9: Repair Loop

If verification fails, do not just say "fix it."

Use this prompt:

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

Maximum repair attempts:

```text
2
```

After two failed repair attempts, mark the workflow as `NEEDS_HUMAN`.

## Stage 10: Fresh-context Review

Open a fresh AI context.

Provide only:

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

## Stage 11: Decision Log

Create:

```text
runs/week5-run-001/decision-log.md
```

Use:

```text
student/artifact-templates/decision-log.md
```

Your job is not to obey every AI suggestion. Your job is to decide.

## Stage 12: Retrospective

Create:

```text
runs/week5-run-001/retrospective.md
```

Use:

```text
student/artifact-templates/retrospective.md
```

## Submission

Submit:

```text
1. Modified project code
2. Complete runs/week5-run-001 folder
3. Verification output
4. Decision log
5. Retrospective
```

## Rubric

| Category | Points |
| --- | ---: |
| Task Contract: clear, testable, scoped | 15 |
| Workflow Spec: stages, actors, permissions, gates, failure policy | 15 |
| Context Packet and Skill Contracts | 10 |
| AI Reconnaissance quality | 10 |
| Implementation Plan and acceptance criteria mapping | 10 |
| Human Approval Gate and approved file scope | 10 |
| Verification Report and evidence mapping | 15 |
| Fresh-context Review quality | 5 |
| Decision Log showing human judgment | 5 |
| Retrospective and Week 6 bridge | 5 |
