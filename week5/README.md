# AIM 5012 Week 5

Topic: AI Coding Workflow on a Real Project.

This public folder contains only the student-facing Week 5 materials.

## Project

```text
Campus Room Booking API
Feature: Waitlist + Cancellation Promotion
```

Students start from a working FastAPI booking API. The starter intentionally
does not include the waitlist feature.

## Student Materials

- `student/AIM5012_Week5_Student_Lab.md` - step-by-step lab instructions.
- `student/campus-room-booking/` - runnable starter project.
- `student/artifact-templates/` - workflow artifact templates.
- `student/AIM5012_Week5_Campus_Room_Booking_Starter.zip` - starter project zip.
- `student/week5-lab-packet/` - expanded full lab packet.
- `student/AIM5012_Week5_Student_Lab_Packet.zip` - full student packet zip.

## Starter Verification

From `student/campus-room-booking/`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
bash scripts/verify.sh
```

The baseline starter should pass before any feature work begins.

## Workflow

Students complete the feature through this workflow:

```text
contract -> reconnaissance -> plan -> approval -> implementation
-> verification -> review -> decision
```

Create the workflow run folder from inside `student/campus-room-booking/`:

```bash
mkdir -p runs/week5-run-001
cp ../artifact-templates/* runs/week5-run-001/
```

Do not ask AI to implement the waitlist feature before completing the contract,
reconnaissance, plan, and approval stages.
