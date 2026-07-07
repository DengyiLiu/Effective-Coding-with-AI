from mcp.server.fastmcp import FastMCP

mcp = FastMCP("course-helper-broken")


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


def evaluate_prompt(prompt: str) -> str:
    """This function is intentionally not exposed because @mcp.tool() is missing."""
    if len(prompt.strip()) < 40:
        return "The prompt is too short."
    return "This prompt may be specific enough."


if __name__ == "__main__":
    mcp.run(transport="stdio")
