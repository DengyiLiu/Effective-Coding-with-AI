# Week 5 课程设计: AI Coding Workflow on a Real Project

## 一句话主线

Week 5 teaches students to turn AI coding from an unstructured conversation
into a controlled engineering workflow.

更适合 slide 的英文版本:

```text
Effective AI coding is not about giving better commands.
It is about designing better control systems around AI work.
```

## 课程定位

Week 5 不再使用 ticket classifier 或 CSV validation 这类单文件任务，而是切换到一个小型但真实的 backend feature:

```text
Project: Campus Room Booking API
Feature: Waitlist + Cancellation Promotion
```

学生学习的核心不是 FastAPI 语法，也不是让 AI 写更多代码，而是:

```text
How do we let AI change existing software without losing control?
```

本周的核心能力是用 contracts, gates, verification, review, evidence 来控制 AI coding work。

## 设计原则

本课程设计采用以下原则:

- 对定义清楚的任务，优先使用可预测 workflow，而不是高自治 agent。
- AI 先理解 codebase, 找 relevant files, 理解 execution flow, 再计划，最后才编辑。
- 复杂任务拆成小阶段，每个阶段有输入、输出、权限和成功标准。
- 测试输出不是终点，学生必须把测试证据映射回 acceptance criteria。
- Human approval gate 不是形式，而是把 scope 和权限变成可执行边界。
- Review 可以由 AI 辅助，但最终判断必须由人记录在 decision log。

## 学习目标

到 Week 5 结束，学生应该能够:

1. 阅读一个已有小型 backend project，并识别 relevant files。
2. 把 product request 写成可测试的 `task-contract.yaml`。
3. 设计一个本地 AI coding workflow，而不是直接让 AI 写代码。
4. 让 AI 先做 repo reconnaissance，再做 implementation plan。
5. 使用 human approval gate 限制 AI 的修改范围。
6. 要求 AI 把每个 acceptance criterion 映射到测试证据。
7. 运行 deterministic verification command。
8. 在测试失败时使用 repair loop，而不是无限制地说 "fix it"。
9. 使用 fresh-context AI review 检查 diff。
10. 用 decision log 说明哪些 AI 建议被接受、修改、拒绝或延后。
11. 理解 Week 5 artifacts 如何变成 Week 6 agent harness 的组件。

## 项目设定

项目名称:

```text
Campus Room Booking API
```

Starter project 已经支持:

```text
- list rooms
- create confirmed bookings
- reject overlapping bookings
- cancel bookings
- list bookings
- run existing tests
```

Week 5 feature:

```text
Existing behavior:
conflict -> reject

New behavior:
conflict -> waitlist
cancel confirmed booking -> promote first waitlisted booking
```

示例流程:

```text
Alice books Room A, 10:00-11:00
-> confirmed

Bob books Room A, 10:00-11:00
-> waitlisted

Carla books Room A, 10:00-11:00
-> waitlisted behind Bob

Alice cancels
-> Bob becomes confirmed
-> Carla remains waitlisted
```

## 为什么这个项目适合 Week 5

| 真实工程难点 | 教学价值 |
| --- | --- |
| 已有系统不能被破坏 | 需要 regression tests |
| 新 feature 涉及状态变化 | 需要 data model 和 state transition |
| cancellation 会触发 promotion | 需要 edge case testing |
| AI 容易扩大 scope | 需要 non-goals 和 human gate |
| API contract 需要保持稳定 | 需要 approval before public interface change |
| 测试必须证明行为 | 需要 verification report |
| AI review 可能误判 | 需要 human decision log |

## Week 5 Artifact System

学生最终提交:

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

这些文件共同构成一个本地版 PR trail。评分重点不是代码量，而是学生是否能控制、验证、审查 AI coding work。

## 两节课结构

Week 5 建议拆成两个 90-minute sessions。

```text
Session 5.1: Design the workflow before coding.
Session 5.2: Execute, verify, repair, review, and reflect.
```

## Session 5.1: Designing the AI Coding Workflow

### 0-8 min - Opening: Why the old way fails

Slide title:

```text
Why "Just Ask AI to Build It" Fails
```

课堂动作:

老师展示坏 prompt:

```text
Add waitlist support to this booking API.
```

学生预测 AI 可能犯的错误:

```text
- rewrite the booking service
- change endpoint names
- remove old conflict behavior without documenting it
- forget cancellation promotion
- add unnecessary dependencies
- update tests only for happy path
- claim the feature works without running tests
```

Takeaway:

```text
The problem is not only prompting.
The problem is missing workflow.
```

### 8-18 min - Project walkthrough

Slide title:

```text
The Project: Campus Room Booking API
```

展示:

```text
app/main.py
app/models.py
app/booking_service.py
tests/
scripts/verify.sh
docs/api-contract.md
```

Live demo:

```bash
bash scripts/verify.sh
```

强调:

```text
We start from working code.
AI's job is to change it safely, not to replace it.
```

### 18-30 min - Feature walkthrough

Slide title:

```text
The Feature: Waitlist + Promotion
```

课堂问题:

```text
What can go wrong?
```

目标答案:

```text
- promotion order wrong
- cancelled waitlisted booking promotes someone incorrectly
- existing cancellation broken
- overlapping logic changed accidentally
- status field inconsistent
- tests pass but API contract changed
```

### 30-42 min - Core concepts

Slide title:

```text
Skill, Workflow, Agent, Harness
```

四个定义:

```text
Skill:
A reusable action with inputs, outputs, permissions, and success criteria.

Workflow:
A fixed sequence of skills, gates, checks, and evidence.

Agent:
A system where the model can decide some next steps dynamically.

Harness:
The control system around AI work: context, tools, permissions, logs,
verification, repair, and review.
```

课程定位:

```text
Week 5 = manual workflow
Week 6 = automated harness
Later = GitHub / CI / PR integration
```

### 42-58 min - Task Contract workshop

Slide title:

```text
Artifact 1: task-contract.yaml
```

学生创建:

```text
runs/week5-run-001/task-contract.yaml
```

教学重点:

```text
A task contract turns a vague request into something testable.
```

课堂产出应包含:

- problem
- user story
- acceptance criteria
- non-goals
- constraints
- verification command
- evidence required

### 58-70 min - Workflow Spec

Slide title:

```text
Artifact 2: workflow-spec.yaml
```

学生创建:

```text
runs/week5-run-001/workflow-spec.yaml
```

教学重点:

```text
The workflow spec is not documentation after the fact.
It is the operating system for AI-assisted coding.
```

### 70-82 min - Context Packet + Skill Contracts

Slide title:

```text
Artifacts 3-4: context-packet.md and skill-contracts.yaml
```

学生创建:

```text
runs/week5-run-001/context-packet.md
runs/week5-run-001/skill-contracts.yaml
```

教学重点:

```text
Context should be staged, not dumped.
Skills should have boundaries, not just instructions.
```

### 82-90 min - Exit ticket

Slide title:

```text
Before Coding: Can We Control the Work?
```

学生回答:

```text
1. What is the highest-risk part of this feature?
2. Which file should AI inspect first?
3. What change should require human approval?
```

课后任务:

```text
Complete task-contract.yaml, workflow-spec.yaml, context-packet.md,
and skill-contracts.yaml.
```

## Session 5.2: Executing, Verifying, Reviewing

### 0-10 min - Recap

Slide title:

```text
From Plan to Evidence
```

回顾:

```text
Task Contract
-> Workflow Spec
-> Context Packet
-> Reconnaissance
-> Plan
-> Human Gate
-> Implementation
-> Verification
-> Review
-> Decision Log
```

### 10-25 min - AI Reconnaissance

Slide title:

```text
Stage 1: AI Reconnaissance
```

学生保存:

```text
runs/week5-run-001/reconnaissance.md
```

老师检查:

```text
Did AI identify the correct service layer?
Did AI understand current conflict behavior?
Did AI identify cancellation logic?
Did AI avoid implementation too early?
```

### 25-38 min - Implementation Plan

Slide title:

```text
Stage 2: Implementation Plan
```

学生保存:

```text
runs/week5-run-001/implementation-plan.md
```

Plan 必须包含:

- goal
- proposed files to modify
- files not to modify
- acceptance criteria mapping
- test plan
- risk notes

### 38-48 min - Human Approval Gate

Slide title:

```text
Stage 3: Human Approval Gate
```

学生保存:

```text
runs/week5-run-001/approval.md
```

教学重点:

```text
Human approval is not a formality.
It is the moment where scope becomes enforceable.
```

### 48-62 min - Implementation

Slide title:

```text
Stage 4: Controlled Implementation
```

规则:

```text
- Implement only the approved plan.
- Stay within approved file scope.
- Do not add dependencies.
- Do not change endpoint names.
- Do not modify scripts/verify.sh.
- Do not delete or weaken existing tests.
- Update existing conflict-rejection tests only when replacing the old 409 behavior with the approved waitlist behavior.
- Add tests for acceptance criteria.
```

学生保存:

```bash
git diff > runs/week5-run-001/diff.patch
```

### 62-72 min - Verification

Slide title:

```text
Stage 5: Verification Report
```

学生运行:

```bash
bash scripts/verify.sh
```

学生保存:

```text
runs/week5-run-001/verification-report.md
```

教学重点:

```text
Passing tests is not enough.
Students must map evidence back to acceptance criteria.
```

### 72-80 min - Repair Loop

Slide title:

```text
Stage 6: Repair Without Scope Creep
```

Policy:

```yaml
repair_policy:
  max_attempts: 2
  must_explain_failure_before_fixing: true
  cannot_modify_tests_to_hide_failure: true
  after_max_attempts: NEEDS_HUMAN
```

### 80-88 min - Fresh-context AI Review + Decision Log

Slide title:

```text
Stage 7: Fresh-context Review
```

给 reviewer 的上下文只包括:

```text
task-contract.yaml
implementation-plan.md
approval.md
diff.patch
verification-report.md
```

学生保存:

```text
runs/week5-run-001/ai-review.md
runs/week5-run-001/decision-log.md
```

教学重点:

```text
AI can review.
Humans decide.
```

### 88-90 min - Bridge to Week 6

Slide title:

```text
From Manual Workflow to Agent Harness
```

映射:

| Week 5 Artifact | Week 6 Harness Component |
| --- | --- |
| `task-contract.yaml` | task validator |
| `workflow-spec.yaml` | state machine |
| `skill-contracts.yaml` | tool / skill registry |
| `context-packet.md` | context builder |
| `approval.md` | human approval gate |
| `scripts/verify.sh` | deterministic verifier |
| `verification-report.md` | trace / evidence |
| `ai-review.md` | reviewer agent |
| `decision-log.md` | oversight record |
| `retrospective.md` | evaluation feedback |

## 作业

Assignment title:

```text
Local AI Coding Workflow Run on a Real Project
```

Student task:

```text
Use AI to add waitlist and cancellation promotion to the Campus Room Booking API.

You must not directly ask AI to implement the feature.

You must execute the workflow:
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision.
```

Required submission:

```text
1. Modified project code
2. Complete runs/week5-run-001 folder
3. Verification output
4. Decision log
5. Retrospective
```

## Rubric

Total: 100 points.

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

Do not emphasize:

```text
number of lines changed
AI tool brand
prompt length
whether the feature is fancy
whether the student used GitHub
```

Emphasize:

```text
Can the student control, verify, and review AI coding work?
```
