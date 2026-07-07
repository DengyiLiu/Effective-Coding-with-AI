# Week 6: Model Context Protocol

## Scope

MCP connects AI systems to project files, tools, APIs, and workflows through explicit server-defined capabilities.

## Core Concepts

### Host

The application the user interacts with. Examples include an AI coding assistant, desktop app, or chat interface.

### Client

The component inside the host that speaks MCP to a server.

### Server

The process that exposes specific tools, resources, or prompts.

## MCP Capabilities

### Tools

Tools are callable actions. A tool can read a project file, run a verification script, evaluate a prompt, or query a service.

### Resources

Resources are stable pieces of context. A resource can be a course requirement file, rubric, API schema, project contract, or documentation page.

### Prompts

Prompts are reusable prompt templates. They standardize common workflows, such as reviewing a project idea or explaining a verification failure.

## Safety Boundary

MCP servers expose specific capabilities. A server should not automatically expose the entire computer, all accounts, or all secrets.

## Demo Set

1. Filesystem access with a configured directory boundary.
2. Python functions exposed as MCP tools.
3. Project verification through an MCP server.
4. Project review with resources, tools, and prompts.
5. Workflow review using project files, verification output, summaries, and repair plans.
