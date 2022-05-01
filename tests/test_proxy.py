"""Tests for classes with proxy pattern."""

from src.design_patterns_in_python.proxy import Person
from src.design_patterns_in_python.proxy import ResponsiblePerson


class TestPerson:
    def test_drink(self):
        p = Person(10)
        assert p.drink() == f"Age {p.age}: drinking"

    def test_drive(self):
        p = Person(10)
        assert p.drive() == f"Age {p.age}: driving"

    def test_drink_and_drive(self):
        p = Person(10)
        assert p.drink_and_drive() == f"Age {p.age}: driving while drunk"


class TestResponsiblePerson:
    def test_drink(self):
        rp = ResponsiblePerson(Person(10))
        assert rp.drink() == f"Age {rp.age}: no drinking: too young"
        rp.age = 20
        assert rp.drink() == f"Age {rp.age}: drinking"

    def test_drive(self):
        rp = ResponsiblePerson(Person(10))
        assert rp.drive() == f"Age {rp.age}: no driving: too young"
        rp.age = 20
        assert rp.drive() == f"Age {rp.age}: driving"

    def test_drink_and_drive(self):
        rp = ResponsiblePerson(Person(10))
        assert rp.drink_and_drive() == f"Age {rp.age}: drink and drive: dead"
        rp.age = 20
        assert rp.drink_and_drive() == f"Age {rp.age}: drink and drive: dead"
