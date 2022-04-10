from unittest import TestCase

from src.design_patterns_in_python.builder import CodeBuilder


class TestBuilder(TestCase):
    @staticmethod
    def preprocess(s: str = "") -> str:
        return s.strip().replace("\r\n", "\n")

    def test_empty(self) -> None:
        cb = CodeBuilder("Foo")
        self.assertEqual(self.preprocess(str(cb)), "class Foo:\n  pass")

    def test_person(self) -> None:
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        self.assertEqual(
            self.preprocess(str(cb)),
            """class Person:\n  def __init__(self):\n    self.name = \"\"\n    self.age = 0""",
        )
