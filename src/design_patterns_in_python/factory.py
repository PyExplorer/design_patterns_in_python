"""Builder pattern."""
from __future__ import annotations  # pragma: no cover


class Person:
    """One person class."""

    def __init__(self, pid: int, name: str) -> None:
        """Initialization."""
        self.id = pid
        self.name = name

    def __str__(self) -> str:
        """String representation for the class."""
        return f"{self.id}, {self.name}"


class PersonFactory:
    """Person factory class"""

    def __init__(self, start_index: int) -> None:
        """Initialization."""
        self.person_id = start_index

    def create_person(self, name: str) -> Person:
        """Main function of the factory."""
        p = Person(self.person_id, name)
        self.person_id += 1
        return p


def main(list_of_names) -> None:  # pragma: no cover
    """Main."""
    factory = PersonFactory(0)
    persons = [factory.create_person(name) for name in list_of_names]
    print(*persons, sep="\n")


if __name__ == "__main__":  # pragma: no cover
    names = ["John", "Marc", "Luiz"]
    main(names)
