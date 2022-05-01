"""Proxy pattern.

A class that functions as an interface to a particular resource. That resource may be remote, expensive to construct,
or may require logging or some other added functionality.
"""
from __future__ import annotations  # pragma: no cover


class Person:
    """Class for any person."""

    __slots__ = ["age"]

    def __init__(self, age: int) -> None:  # noqa: D107
        self.age = age

    def drink(self) -> str:  # noqa: D102
        return f"Age {self.age}: drinking"

    def drive(self) -> str:  # noqa: D102
        return f"Age {self.age}: driving"

    def drink_and_drive(self) -> str:  # noqa: D102
        return f"Age {self.age}: driving while drunk"


class ResponsiblePerson:
    """Class for responsible person."""

    def __init__(self, person: Person) -> None:  # noqa: D107
        self.person = person

    @property
    def age(self) -> int:  # noqa: D102
        return self.person.age

    @age.setter
    def age(self, value: int) -> None:  # noqa: D102
        self.person.age = value

    def drink(self) -> str:  # noqa: D102
        if self.age >= 18:
            return f"Age {self.age}: drinking"
        return f"Age {self.age}: no drinking: too young"

    def drive(self) -> str:  # noqa: D102
        if self.age >= 16:
            return f"Age {self.age}: driving"
        return f"Age {self.age}: no driving: too young"

    def drink_and_drive(self) -> str:  # noqa: D102
        return f"Age {self.age}: drink and drive: dead"


def main():  # noqa: D103, pragma: no cover
    p = Person(10)
    rp = ResponsiblePerson(p)
    print(rp.drive())
    print(rp.drink())
    print(rp.drink_and_drive())
    rp.age = 20
    print(rp.drive())
    print(rp.drink())
    print(rp.drink_and_drive())


if __name__ == "__main__":  # pragma: no cover
    main()
