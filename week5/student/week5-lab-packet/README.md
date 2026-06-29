# AIM 5012 Week 5 Student Lab Packet

This packet contains everything students need for the Week 5 local AI coding
workflow lab.

## Contents

- `AIM5012_Week5_Student_Lab.md` - step-by-step lab instructions.
- `campus-room-booking/` - FastAPI starter project.
- `artifact-templates/` - files to copy into `runs/week5-run-001/`.

## Start Here

```bash
cd campus-room-booking
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
```

The starter project should pass before any feature work begins.

## Create The Workflow Folder

From inside `campus-room-booking/`:

```bash
mkdir -p runs/week5-run-001
cp ../artifact-templates/* runs/week5-run-001/
```

Then follow `AIM5012_Week5_Student_Lab.md`.

## Important Rule

Do not ask AI to implement the waitlist feature immediately. The assignment is
to execute the workflow:

```text
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision
```
