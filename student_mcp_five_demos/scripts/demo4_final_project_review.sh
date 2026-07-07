#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

exec npx -y @modelcontextprotocol/inspector \
  uv --cache-dir "$ROOT_DIR/.uv-cache" run python demos/final-project-review/server.py
