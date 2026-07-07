from __future__ import annotations

from dataclasses import dataclass, field

VALID_STATUSES = {"waiting", "admitted", "declined"}


def normalize_email(email: str) -> str:
    """Return the canonical form used as the waitlist key."""
    return email.strip().lower()


@dataclass
class WaitlistManager:
    entries: dict[str, dict[str, str]] = field(default_factory=dict)

    def add_student(self, email: str, display_name: str) -> str:
        normalized_email = normalize_email(email)
        clean_name = display_name.strip()

        if not normalized_email:
            raise ValueError("Email is required.")
        if not clean_name:
            raise ValueError("Display name is required.")

        self.entries[normalized_email] = {
            "email": normalized_email,
            "display_name": clean_name,
            "status": "waiting",
        }
        return normalized_email

    def update_status(self, email: str, status: str) -> None:
        normalized_email = normalize_email(email)
        clean_status = status.strip().lower()

        if clean_status not in VALID_STATUSES:
            raise ValueError(f"Unknown status: {status}")
        if normalized_email not in self.entries:
            raise KeyError(f"Student not found: {email}")

        self.entries[normalized_email]["status"] = clean_status

    def get_student(self, email: str) -> dict[str, str]:
        normalized_email = normalize_email(email)
        if normalized_email not in self.entries:
            raise KeyError(f"Student not found: {email}")
        return dict(self.entries[normalized_email])

    def summary(self) -> dict[str, int]:
        counts = {status: 0 for status in sorted(VALID_STATUSES)}
        for entry in self.entries.values():
            counts[entry["status"]] += 1
        return counts
