from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic import AnyUrl

ROOT = Path(__file__).parents[1].resolve()


def _text_from_result(result: object) -> str:
    content = getattr(result, "content", [])
    parts: list[str] = []
    for item in content:
        text = getattr(item, "text", None)
        parts.append(text if text is not None else str(item))
    return "\n".join(parts)


async def _session_for(server_path: Path):
    params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)],
        cwd=str(ROOT),
    )
    return stdio_client(params)


async def validate_course_helper() -> None:
    async with await _session_for(ROOT / "demos/course-helper/server.py") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = {tool.name for tool in tools.tools}
            assert {"get_week_topic", "evaluate_prompt"} <= tool_names

            topic_result = await session.call_tool("get_week_topic", {"week": 6})
            assert "Model Context Protocol" in _text_from_result(topic_result)

            prompt_result = await session.call_tool("evaluate_prompt", {"prompt": "Build me an app"})
            assert "Suggestions:" in _text_from_result(prompt_result)

    async with await _session_for(ROOT / "demos/course-helper/server_debug_missing_decorator.py") as (
        read,
        write,
    ):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = {tool.name for tool in tools.tools}
            assert "get_week_topic" in tool_names
            assert "evaluate_prompt" not in tool_names

    print("course-helper: ok")


async def validate_week5_verify() -> None:
    async with await _session_for(ROOT / "demos/week5-verify/server.py") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = {tool.name for tool in tools.tools}
            assert {"list_project_files", "read_project_file", "run_verify", "explain_verify_result"} <= tool_names

            files_result = await session.call_tool("list_project_files", {})
            files_text = _text_from_result(files_result)
            assert "task-contract.yaml" in files_text
            assert "scripts/verify.sh" in files_text

            contract_result = await session.call_tool("read_project_file", {"relative_path": "task-contract.yaml"})
            assert "waitlist-status-helper" in _text_from_result(contract_result)

            verify_result = await session.call_tool("run_verify", {})
            verify_text = _text_from_result(verify_result)
            assert "exit_code: 0" in verify_text
            assert "Ran 15 tests" in verify_text

            explain_result = await session.call_tool("explain_verify_result", {"output": verify_text})
            assert "Verification passed" in _text_from_result(explain_result)

            resources = await session.list_resources()
            resource_uris = {str(resource.uri) for resource in resources.resources}
            assert "week5://task-contract" in resource_uris

    print("week5-verify: ok")


async def validate_final_project_review() -> None:
    async with await _session_for(ROOT / "demos/final-project-review/server.py") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = {tool.name for tool in tools.tools}
            assert "review_project_idea" in tool_names

            resources = await session.list_resources()
            resource_uris = {str(resource.uri) for resource in resources.resources}
            assert "course://final-project/requirements" in resource_uris
            assert "course://final-project/rubric" in resource_uris

            prompts = await session.list_prompts()
            prompt_names = {prompt.name for prompt in prompts.prompts}
            assert "final_project_review_prompt" in prompt_names

            weak_result = await session.call_tool(
                "review_project_idea",
                {
                    "topic": "AI website builder",
                    "abstract": "We want to build a website using AI.",
                },
            )
            assert "Project review feedback:" in _text_from_result(weak_result)

    print("final-project-review: ok")


async def validate_advanced_workflow_harness() -> None:
    async with await _session_for(ROOT / "demos/advanced-workflow-harness/server.py") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = {tool.name for tool in tools.tools}
            assert {
                "list_project_files",
                "read_project_file",
                "run_verify",
                "summarize_test_failures",
                "generate_repair_plan",
            } <= tool_names

            resources = await session.list_resources()
            resource_uris = {str(resource.uri) for resource in resources.resources}
            assert {
                "course://week5/task-contract",
                "course://week5/waitlist-spec",
                "course://week5/project-readme",
                "course://week5/test-summary",
            } <= resource_uris

            spec_result = await session.read_resource(AnyUrl("course://week5/waitlist-spec"))
            spec_text = "\n".join(getattr(content, "text", "") for content in spec_result.contents)
            assert "Allowed statuses" in spec_text

            files_result = await session.call_tool("list_project_files", {})
            files_text = _text_from_result(files_result)
            assert "docs/waitlist-spec.md" in files_text
            assert "app/waitlist.py" in files_text

            verify_result = await session.call_tool("run_verify", {})
            verify_text = _text_from_result(verify_result)
            assert "exit_code: 0" in verify_text
            assert "Ran 15 tests" in verify_text

            summary_result = await session.call_tool("summarize_test_failures", {"output": verify_text})
            summary_text = _text_from_result(summary_result)
            assert "status: passed" in summary_text

            plan_result = await session.call_tool("generate_repair_plan", {"failure_summary": summary_text})
            assert "repair_needed: no" in _text_from_result(plan_result)

    print("advanced-workflow-harness: ok")


async def main() -> None:
    await validate_course_helper()
    await validate_week5_verify()
    await validate_final_project_review()
    await validate_advanced_workflow_harness()
    print("All MCP server validations passed.")


if __name__ == "__main__":
    asyncio.run(main())
