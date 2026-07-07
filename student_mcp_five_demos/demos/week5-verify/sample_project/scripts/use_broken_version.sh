#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cp "$PROJECT_DIR/broken_examples/waitlist_missing_normalization.py" "$PROJECT_DIR/app/waitlist.py"

echo "The broken waitlist implementation is now active."
