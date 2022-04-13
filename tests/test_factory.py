"""Tests for classes with factory pattern."""
from src.design_patterns_in_python.factory import Person
from src.design_patterns_in_python.factory import PersonFactory


class TestPerson:
    """Test case for one person."""

    def test_person(self) -> None:
        """Test case for field with all args."""
        p = Person(0, "foo")
        assert str(p) == "0, foo"


class TestFactory:
    """Test case for factory."""

    def test_factory_0(self) -> None:
        """Test creating two persons with 0 starting index."""
        factory = PersonFactory(0)
        person_1 = factory.create_person("foo")
        person_2 = factory.create_person("boo")
        assert person_1.name == "foo"
        assert person_1.id == 0
        assert person_2.name == "boo"
        assert person_2.id == 1

    def test_factory_1(self) -> None:
        """Test creating two persons with 1 staring index."""
        factory = PersonFactory(1)
        person_1 = factory.create_person("foo")
        person_2 = factory.create_person("boo")
        assert person_1.name == "foo"
        assert person_1.id == 1
        assert person_2.name == "boo"
        assert person_2.id == 2
