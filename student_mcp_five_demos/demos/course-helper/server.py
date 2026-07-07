from mcp.server.fastmcp import FastMCP

mcp = FastMCP("course-helper")


@mcp.tool()
def get_week_topic(week: int) -> str:
    """Return the main topic for a course week."""
    topics = {
        1: "AI coding mindset and prompting",
        2: "Skills and structured AI workflows",
        3: "Webpage generation with AI",
        4: "Python notebook pipeline",
        5: "Agent workflow and verification",
        6: "Model Context Protocol",
    }
    return topics.get(week, "Unknown week.")


@mcp.tool()
def evaluate_prompt(prompt: str) -> str:
    """Evaluate whether a prompt is specific enough for AI-assisted coding."""
    lower_prompt = prompt.lower()
    feedback: list[str] = []

    if len(prompt.strip()) < 40:
        feedback.append("The prompt is too short.")
    if "goal" not in lower_prompt:
        feedback.append("Add a clear goal.")
    if "context" not in lower_prompt:
        feedback.append("Add context.")
    if "output" not in lower_prompt and "format" not in lower_prompt:
        feedback.append("Specify the output format.")
    if "test" not in lower_prompt and "verify" not in lower_prompt:
        feedback.append("Add a testing or verification step.")
    if "constraint" not in lower_prompt and "limit" not in lower_prompt:
        feedback.append("Add one constraint or limit.")

    if not feedback:
        return "This prompt is reasonably specific."

    return "Suggestions:\n- " + "\n- ".join(feedback)


if __name__ == "__main__":
    mcp.run(transport="stdio")
