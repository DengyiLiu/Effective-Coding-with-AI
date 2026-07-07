from __future__ import annotations

import re
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("week5-verify")

PROJECT_ROOT = (Path(__file__).parent / "sample_project").resolve()


def _safe_project_path(relative_path: str) -> Path:
    requested = Path(relative_path)
    if requested.is_absolute():
        raise ValueError("Use a relative path inside the sample project.")

    resolved = (PROJECT_ROOT / requested).resolve()
    if PROJECT_ROOT not in resolved.parents and resolved != PROJECT_ROOT:
        raise ValueError("Path is outside the sample project boundary.")
    if not resolved.exists():
        raise FileNotFoundError(f"File not found: {relative_path}")
    if resolved.is_dir():
        raise IsADirectoryError(f"Path is a directory: {relative_path}")
    return resolved


@mcp.tool()
def list_project_files() -> str:
    """List files in the Week 5 sample project."""
    files: list[str] = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if path.is_dir():
            continue
        if "__pycache__" in path.parts:
            continue
        if path.name.endswith(".pyc"):
            continue
        files.append(path.relative_to(PROJECT_ROOT).as_posix())
    return "\n".join(files)


@mcp.tool()
def read_project_file(relative_path: str) -> str:
    """Read a file from the Week 5 sample project by relative path."""
    path = _safe_project_path(relative_path)
    return path.read_text(encoding="utf-8")


@mcp.tool()
def run_verify() -> str:
    """Run the Week 5 verification script and return stdout, stderr, and exit code."""
    script = PROJECT_ROOT / "scripts" / "verify.sh"
    result = subprocess.run(
        ["bash", str(script)],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )

    sections = [
        f"exit_code: {result.returncode}",
        "stdout:",
        result.stdout.strip() or "(empty)",
        "stderr:",
        result.stderr.strip() or "(empty)",
    ]
    return "\n".join(sections)


@mcp.tool()
def explain_verify_result(output: str) -> str:
    """Explain verification output in beginner-friendly language."""
    lowered = output.lower()
    ran_match = re.search(r"ran\s+(\d+)\s+tests?", output, flags=re.IGNORECASE)
    test_count = ran_match.group(1) if ran_match else "the"

    if "exit_code: 0" in output and "\nok" in lowered:
        return (
            f"Verification passed. The project ran {test_count} tests successfully. "
            "The next step is to connect this evidence back to the task contract and explain "
            "which requirements are covered by the tests."
        )

    if "assertionerror" in lowered or "failed" in lowered or "fail:" in lowered:
        return (
            "Verification failed. Read the first failing test name, then compare the expected "
            "behavior with the current implementation. Do not start by rewriting everything. "
            "Start by finding the smallest behavior that violates the contract."
        )

    if "modulenotfounderror" in lowered or "importerror" in lowered:
        return (
            "The verification script did not reach the behavior tests because Python could not "
            "import something. Check the working directory, package names, and import paths."
        )

    return (
        "The verification result is unclear. First check the exit code. Then check stdout and "
        "stderr for the earliest error message. Use that first error as the next debugging target."
    )


@mcp.resource("week5://task-contract")
def task_contract() -> str:
    """Return the Week 5 sample project task contract."""
    return (PROJECT_ROOT / "task-contract.yaml").read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run(transport="stdio")
