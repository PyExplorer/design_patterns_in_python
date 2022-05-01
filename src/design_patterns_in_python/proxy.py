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
        return "drinking"

    def drive(self) -> str:  # noqa: D102
        return "driving"

    def drink_and_drive(self) -> str:  # noqa: D102
        return "driving while drunk"


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
            return "drinking"
        return "no drinking: too young"

    def drive(self) -> str:  # noqa: D102
        if self.age >= 16:
            return "driving"
        return "not driving: too young"

    def drink_and_drive(self) -> str:  # noqa: D102
        return "drink and drive: dead"


def main():  # noqa: D103
    p = Person(10)  # pragma: no cover
    rp = ResponsiblePerson(p)  # pragma: no cover
    print(f"For age {rp.age}")
    print(rp.drive())  # pragma: no cover
    print(rp.drink())  # pragma: no cover
    print(rp.drink_and_drive())  # pragma: no cover
    rp.age = 20
    print(f"For age {rp.age}")
    print(rp.drive())  # pragma: no cover
    print(rp.drink())  # pragma: no cover
    print(rp.drink_and_drive())  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    main()
