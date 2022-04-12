"""Tests for classes with builder pattern."""
from src.design_patterns_in_python.builder import CodeBuilder
from src.design_patterns_in_python.builder import OneField


class TestOneField:
    """Test case for one field."""

    def test_field(self) -> None:
        """Test case for field with all args."""
        field = OneField("foo", "boo")
        assert str(field) == "self.foo = boo"

    def test_creation_empty_field(self) -> None:
        """Test case for field without args."""
        field = OneField()
        assert str(field) == "self. = "


class TestBuilder:
    """Test case for builder."""

    @staticmethod
    def __preprocess(s: str = "") -> str:
        return s.strip().replace("\r\n", "\n")

    def test_empty(self) -> None:
        """Test for empty class."""
        cb = CodeBuilder("Foo")
        assert self.__preprocess(str(cb)) == "class Foo:\n  pass"

    def test_person(self) -> None:
        """Test for full class."""
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        assert (
            self.__preprocess(str(cb))
            == """class Person:\n  def __init__(self):\n    self.name = \"\"\n    self.age = 0"""
        )
