# Repository Guidelines

## Project Structure & Module Organization

This repository contains AIM 5012 Week 5 course materials and a runnable starter
project.

- `README.md` maps the Week 5 package.
- `source/` contains course design notes and the starter project specification.
- `instructor/` contains instructor-facing guides and slide blueprints.
- `student/AIM5012_Week5_Student_Lab.md` is the student-facing lab handout.
- `student/artifact-templates/` contains workflow artifact templates.
- `student/campus-room-booking/` is the FastAPI starter project.
- `student/AIM5012_Week5_Campus_Room_Booking_Starter.zip` is the distributable starter archive.

In the starter project, source code lives in `app/`, tests in `tests/`, docs in
`docs/`, and the verification script in `scripts/verify.sh`.

## Build, Test, and Development Commands

From `student/campus-room-booking/`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
python -m uvicorn app.main:app --reload
```

`scripts/verify.sh` runs the deterministic pytest suite. The `uvicorn` command
starts the local API at `http://127.0.0.1:8000/docs`.

## Coding Style & Naming Conventions

Use concise, beginner-readable Python. Prefer explicit functions over clever
abstractions. Use four-space indentation, type hints where helpful, and
snake_case for modules, functions, variables, and test names.

Keep course documents in Markdown with clear headings, short paragraphs, and
copyable command blocks. Avoid unrelated rewrites of existing course materials.

## Testing Guidelines

Tests use `pytest` and FastAPI `TestClient`. Name test files `test_*.py` and test
functions `test_*`. Add or update tests with any behavior change.

Do not delete tests, weaken assertions, skip tests to pass verification, or
modify `scripts/verify.sh` without explicit approval.

## Commit & Pull Request Guidelines

No local git history is available here, so no repository-specific commit pattern
can be inferred. Use concise imperative commit messages such as `Add Week 5
starter API` or `Update waitlist workflow templates`.

Pull requests should describe the course-material change, list edited files,
include verification output, and note whether the starter zip must be
regenerated.

## Agent-Specific Instructions

Keep edits scoped to Week 5. Preserve the teaching objective: students should
control AI coding through contracts, gates, verification, review, and evidence.
Do not implement the waitlist feature in the starter project unless explicitly
asked; it is the student lab task.
