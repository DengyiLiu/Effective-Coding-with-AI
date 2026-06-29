#!/usr/bin/env bash
set -euo pipefail

python -m py_compile app/*.py
python -m pytest -q
