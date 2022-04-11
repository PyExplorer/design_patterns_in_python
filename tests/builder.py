"""Tests for classes with builder pattern."""
from unittest import TestCase

from src.design_patterns_in_python.builder import CodeBuilder


class TestBuilder(TestCase):
    """Test case for builder."""

    @staticmethod
    def __preprocess(s: str = "") -> str:
        return s.strip().replace("\r\n", "\n")

    def test_empty(self) -> None:
        """Test for empty class."""
        cb = CodeBuilder("Foo")
        self.assertEqual(self.__preprocess(str(cb)), "class Foo:\n  pass")

    def test_person(self) -> None:
        """Test for full class."""
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        self.assertEqual(
            self.__preprocess(str(cb)),
            """class Person:\n  def __init__(self):\n    self.name = \"\"\n    self.age = 0""",
        )
