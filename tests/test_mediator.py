"""Tests for classes with mediator."""
from src.design_patterns_in_python.mediator import Mediator
from src.design_patterns_in_python.mediator import Participant
from unittest import TestCase


class TestSuite(TestCase):
    """Test for Mediator"""

    def test(self):  # noqa: D102
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)
