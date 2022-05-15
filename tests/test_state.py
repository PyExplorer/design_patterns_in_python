from unittest import TestCase
from src.design_patterns_in_python.state import CombinationLock


class TestSuite(TestCase):
    """Tests for State pattern."""

    def test_success(self):  # noqa: D102
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(3)
        self.assertEqual("123", cl.status)
        cl.enter_digit(4)
        self.assertEqual("1234", cl.status)
        cl.enter_digit(5)
        self.assertEqual("OPEN", cl.status)

    def test_failure(self):  # noqa: D102
        cl = CombinationLock([1, 2, 3])
        self.assertEqual("LOCKED", cl.status)
        cl.enter_digit(1)
        self.assertEqual("1", cl.status)
        cl.enter_digit(2)
        self.assertEqual("12", cl.status)
        cl.enter_digit(5)
        self.assertEqual("ERROR", cl.status)
