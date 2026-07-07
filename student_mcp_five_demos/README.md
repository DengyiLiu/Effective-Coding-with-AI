# MCP Five Demo Pack

This repository contains five runnable Model Context Protocol (MCP) demos.

## Requirements

- Python 3.11 or newer
- `uv`
- Node.js and npm

The launch scripts use `npx` for MCP Inspector and, in Demo 1, the official filesystem MCP server.

## Setup

```bash
bash scripts/setup.sh
```

Optional validation for the Python MCP servers:

```bash
uv --cache-dir .uv-cache run python scripts/validate_mcp_servers.py
```

## Demo Commands

| Demo | Command |
| --- | --- |
| 1. Filesystem MCP | `bash scripts/demo1_filesystem.sh` |
| 1. Filesystem MCP with wrong path | `bash scripts/demo1_wrong_path.sh` |
| 2. Course Helper starter | `bash scripts/demo2_course_helper_starter.sh` |
| 2. Course Helper complete | `bash scripts/demo2_course_helper.sh` |
| 2. Course Helper broken registration | `bash scripts/demo2_course_helper_broken.sh` |
| 3. Week 5 Verify | `bash scripts/demo3_week5_verify.sh` |
| 4. Final Project Review | `bash scripts/demo4_final_project_review.sh` |
| 5. Advanced Workflow Harness | `bash scripts/demo5_advanced_workflow_harness.sh` |

After a launch script starts, use the MCP Inspector URL printed in the terminal.

## Demo Reference

### 1. Filesystem MCP

Uses the official `@modelcontextprotocol/server-filesystem` package with `course_docs/` as the allowed directory.

Main command:

```bash
bash scripts/demo1_filesystem.sh
```

Boundary-check command:

```bash
bash scripts/demo1_wrong_path.sh
```

### 2. Course Helper MCP Server

Files:

- `demos/course-helper/server_starter.py`
- `demos/course-helper/server.py`
- `demos/course-helper/server_debug_missing_decorator.py`

Tools in the complete server:

- `get_week_topic(week)`
- `evaluate_prompt(prompt)`

Example payload:

```json
{
  "prompt": "Build me an app"
}
```

### 3. Week 5 Verify MCP Server

Path:

```text
demos/week5-verify/
```

Tools:

- `list_project_files()`
- `read_project_file(relative_path)`
- `run_verify()`
- `explain_verify_result(output)`

Resource:

- `week5://task-contract`

Sample project helper scripts:

```bash
bash demos/week5-verify/sample_project/scripts/use_broken_version.sh
bash demos/week5-verify/sample_project/scripts/use_passing_version.sh
```

### 4. Final Project Review MCP Server

Path:

```text
demos/final-project-review/
```

Tool:

- `review_project_idea(topic, abstract)`

Resources:

- `course://final-project/requirements`
- `course://final-project/rubric`

Prompt:

- `final_project_review_prompt(topic, abstract)`

Example payload:

```json
{
  "topic": "AI-assisted waitlist management dashboard",
  "abstract": "This project builds a small dashboard that helps an admissions team track waitlist status. We will use AI tools to plan the data model, generate the FastAPI backend, debug failing tests, and create a final demo. The project will include a verification script and a short presentation explaining how AI assisted the workflow."
}
```

### 5. Advanced Workflow Harness

Path:

```text
demos/advanced-workflow-harness/
```

Resources:

- `course://week5/task-contract`
- `course://week5/waitlist-spec`
- `course://week5/project-readme`
- `course://week5/test-summary`

Tools:

- `list_project_files()`
- `read_project_file(path)`
- `run_verify()`
- `summarize_test_failures(output)`
- `generate_repair_plan(failure_summary)`

This server reads, inspects, summarizes, verifies, and produces repair plans. It does not edit files.

## Folder Map

```text
course_docs/
demos/
  filesystem/
  course-helper/
  week5-verify/
  final-project-review/
  advanced-workflow-harness/
scripts/
pyproject.toml
uv.lock
```

## GitHub Notes

Generated files are excluded by `.gitignore`:

- `.venv/`
- `.uv-cache/`
- `__pycache__/`
- `*.pyc`
- `.DS_Store`
