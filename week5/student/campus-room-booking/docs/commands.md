# Commands

## Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run Verification

```bash
source .venv/bin/activate
bash scripts/verify.sh
```

## Run Tests Directly

```bash
source .venv/bin/activate
python -m pytest
```

## Run Development Server

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Notes

The project uses in-memory storage. Restarting the Python process resets rooms
and bookings.
