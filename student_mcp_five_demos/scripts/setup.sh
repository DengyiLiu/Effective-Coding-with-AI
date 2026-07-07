#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Installing Python dependencies with uv..."
uv --cache-dir "$ROOT_DIR/.uv-cache" sync

echo
echo "Setup complete."
echo "Next: run one of the demo scripts, for example:"
echo "  bash scripts/demo2_course_helper.sh"
