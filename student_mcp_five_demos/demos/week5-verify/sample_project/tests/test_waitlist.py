import unittest

from app.waitlist import WaitlistManager, normalize_email


class NormalizeEmailTests(unittest.TestCase):
    def test_lowercases_email(self):
        self.assertEqual(normalize_email("STUDENT@EXAMPLE.COM"), "student@example.com")

    def test_trims_spaces(self):
        self.assertEqual(normalize_email("  student@example.com  "), "student@example.com")

    def test_keeps_internal_characters(self):
        self.assertEqual(normalize_email("first.last+tag@example.com"), "first.last+tag@example.com")


class AddStudentTests(unittest.TestCase):
    def test_add_student_returns_normalized_key(self):
        manager = WaitlistManager()
        key = manager.add_student("  A@Example.COM ", "Ava")
        self.assertEqual(key, "a@example.com")

    def test_add_student_stores_display_name(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", " Ava Chen ")
        self.assertEqual(manager.get_student("a@example.com")["display_name"], "Ava Chen")

    def test_add_student_defaults_to_waiting(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        self.assertEqual(manager.get_student("a@example.com")["status"], "waiting")

    def test_add_student_rejects_blank_email(self):
        manager = WaitlistManager()
        with self.assertRaises(ValueError):
            manager.add_student("  ", "Ava")

    def test_add_student_rejects_blank_display_name(self):
        manager = WaitlistManager()
        with self.assertRaises(ValueError):
            manager.add_student("a@example.com", "  ")


class StatusTests(unittest.TestCase):
    def test_update_status_to_admitted(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        manager.update_status("a@example.com", "admitted")
        self.assertEqual(manager.get_student("a@example.com")["status"], "admitted")

    def test_update_status_normalizes_email_lookup(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        manager.update_status(" A@EXAMPLE.COM ", "declined")
        self.assertEqual(manager.get_student("a@example.com")["status"], "declined")

    def test_update_status_normalizes_status_text(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        manager.update_status("a@example.com", " ADMITTED ")
        self.assertEqual(manager.get_student("a@example.com")["status"], "admitted")

    def test_update_status_rejects_unknown_status(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        with self.assertRaises(ValueError):
            manager.update_status("a@example.com", "maybe")

    def test_update_status_rejects_unknown_student(self):
        manager = WaitlistManager()
        with self.assertRaises(KeyError):
            manager.update_status("missing@example.com", "admitted")


class SummaryTests(unittest.TestCase):
    def test_summary_starts_with_zero_counts(self):
        manager = WaitlistManager()
        self.assertEqual(manager.summary(), {"admitted": 0, "declined": 0, "waiting": 0})

    def test_summary_counts_each_status(self):
        manager = WaitlistManager()
        manager.add_student("a@example.com", "Ava")
        manager.add_student("b@example.com", "Ben")
        manager.add_student("c@example.com", "Cam")
        manager.update_status("b@example.com", "admitted")
        manager.update_status("c@example.com", "declined")
        self.assertEqual(manager.summary(), {"admitted": 1, "declined": 1, "waiting": 1})


if __name__ == "__main__":
    unittest.main()
