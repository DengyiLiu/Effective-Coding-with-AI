#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cp "$PROJECT_DIR/passing_examples/waitlist.py" "$PROJECT_DIR/app/waitlist.py"

echo "The passing waitlist implementation is now active."
