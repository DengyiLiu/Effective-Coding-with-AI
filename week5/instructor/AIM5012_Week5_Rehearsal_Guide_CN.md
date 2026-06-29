# AIM 5012 Week 5 课前预演指南

用途：老师在上课前自己完整跑一遍 Week 5，确认学生会看到什么、AI 容易怎么偏、哪些地方需要人工把关。

建议至少预演一次完整流程。第一次不要追求讲课节奏，目标是理解项目和 workflow。

## 0. 准备位置

从 Week 5 根目录开始：

```bash
cd /Users/liudengyi/Documents/adjunct/summer2026/week5
```

进入 starter 项目：

```bash
cd student/campus-room-booking
```

如果你想模拟学生从 zip 开始，可以解压：

```bash
cd ../..
mkdir -p /tmp/week5-rehearsal
cp student/AIM5012_Week5_Campus_Room_Booking_Starter.zip /tmp/week5-rehearsal/
cd /tmp/week5-rehearsal
unzip AIM5012_Week5_Campus_Room_Booking_Starter.zip
cd campus-room-booking
```

注意：zip 只包含 starter project。workflow artifact 模板在原 repo 的 `student/artifact-templates/`。

## 1. 安装并跑 baseline

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
```

你应该看到：

```text
15 passed
```

可能会出现一个 FastAPI/Starlette deprecation warning。它不是本课重点，也不是失败。

## 2. 手动体验 baseline API

启动服务：

```bash
python -m uvicorn app.main:app --reload
```

打开：

```text
http://127.0.0.1:8000/docs
```

建议你手动试三件事：

1. `GET /rooms` 返回三个 rooms。
2. `POST /bookings` 创建 Alice 的 confirmed booking。
3. 用同一 room/time 创建 Bob 的 booking，当前应返回 `409 Conflict`。

这一步的教学意义：学生要先看到“项目已经工作”，以及“旧行为是 conflict -> reject”。

## 3. 创建 workflow run folder

如果你在原 repo 的 `student/campus-room-booking/` 下预演：

```bash
mkdir -p runs/week5-run-001
cp ../artifact-templates/* runs/week5-run-001/
```

如果你在 `/tmp/week5-rehearsal/campus-room-booking` 下预演，需要从原 repo 复制模板：

```bash
mkdir -p runs/week5-run-001
cp /Users/liudengyi/Documents/adjunct/summer2026/week5/student/artifact-templates/* runs/week5-run-001/
```

确认：

```bash
find runs/week5-run-001 -maxdepth 1 -type f | sort
```

## 4. 第一轮不要让 AI 写代码

先给 AI 坏 prompt，用于课堂讨论：

```text
Add waitlist support to this booking API.
```

不要真的接受它直接改代码。你要观察它可能会：

- 直接改 service，不先读 tests
- 忽略 cancellation promotion
- 改 endpoint 或 schema
- 改 verification script
- 只加 happy path tests

课堂 takeaway：

```text
The problem is not only prompting. The problem is missing workflow.
```

## 5. 正式执行 reconnaissance

把下面 prompt 给 AI：

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

保存输出到：

```text
runs/week5-run-001/reconnaissance.md
```

你要重点检查 AI 是否识别：

- `app/booking_service.py` 是核心修改点
- 当前 overlap 是 `409 Conflict`
- cancellation 只标记 cancelled，没有 promotion
- `test_existing_behavior.py` 里有旧 behavior regression

## 6. 生成 implementation plan

Prompt：

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

保存到：

```text
runs/week5-run-001/implementation-plan.md
```

你要拒绝过大的计划。合理计划通常只动：

- `app/models.py`
- `app/booking_service.py`
- `app/schemas.py` 如果需要
- `tests/test_booking_create.py`
- `tests/test_existing_behavior.py`
- 新增 `tests/test_waitlist.py`
- `docs/api-contract.md`

不应修改：

- `scripts/verify.sh`
- `requirements.txt`
- unrelated endpoints

## 7. 写 human approval

编辑：

```text
runs/week5-run-001/approval.md
```

重点写清楚：

- 批准哪些文件可以改
- 不准改 `scripts/verify.sh`
- 旧 conflict-rejection tests 可以改，但只能改成 waitlist 行为断言
- 不准删除或弱化测试

这一步是课堂核心。Approval 不是“同意 AI 做”，而是把权限边界写下来。

## 8. 让 AI 实现

Prompt：

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

实现后保存 diff：

```bash
git diff > runs/week5-run-001/diff.patch
```

如果没有 git：

```bash
diff -ru app tests docs > runs/week5-run-001/diff.patch
```

## 9. 验证

```bash
bash scripts/verify.sh
```

把输出写入：

```text
runs/week5-run-001/verification-report.md
```

你要检查学生能不能把 evidence 映射到 acceptance criteria：

- AC1 available -> confirmed
- AC2 occupied -> waitlisted
- AC3 waitlist FIFO
- AC4 cancel confirmed no waitlist
- AC5 cancel confirmed promotes earliest waitlisted
- AC6 cancel waitlisted does not promote
- AC7 rooms unchanged
- AC8 confirmed creation backward compatible
- AC9 cancellation backward compatible

## 10. 如果失败，跑 repair loop

不要让 AI 直接 “fix it”。先让它解释失败：

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

最多两轮。两轮后还失败，就标记 `NEEDS_HUMAN`。

## 11. Fresh-context review

开一个新的 AI 上下文，只给：

```text
task-contract.yaml
implementation-plan.md
approval.md
diff.patch
verification-report.md
```

Prompt：

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

保存到：

```text
runs/week5-run-001/ai-review.md
```

然后写：

```text
runs/week5-run-001/decision-log.md
```

## 12. 你预演时要特别观察的问题

1. 学生是否会太早让 AI 写代码。
2. AI 是否会建议改 verification script。
3. AI 是否知道旧 `409 Conflict` 行为需要被 task contract 明确替换。
4. AI 是否覆盖了 cancellation promotion 的 edge case。
5. 学生是否能区分“测试通过”和“AC 有证据”。
6. Fresh-context review 是否能发现 plan/diff 不一致。

## 13. 预演完成标准

你自己的 rehearsal run 完成时，应有：

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

如果你只想快速熟悉项目，至少完成：

- baseline verification
- API docs 手动试一次
- reconnaissance
- implementation plan
- approval

这样就足够知道课堂上学生会卡在哪里。
