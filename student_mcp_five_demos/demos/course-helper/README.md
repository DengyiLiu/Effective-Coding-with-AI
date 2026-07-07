# Demo 2: Course Helper MCP Server

## Files

- `server_starter.py`: server with `get_week_topic`.
- `server.py`: complete server with `get_week_topic` and `evaluate_prompt`.
- `server_debug_missing_decorator.py`: version where `evaluate_prompt` is not registered as an MCP tool.

## Commands

```bash
bash scripts/demo2_course_helper_starter.sh
```

```bash
bash scripts/demo2_course_helper.sh
```

```bash
bash scripts/demo2_course_helper_broken.sh
```

## Example Payload

```json
{
  "week": 6
}
```

```json
{
  "prompt": "Build me an app"
}
```
