"""Builder pattern."""
from __future__ import annotations  # pragma: no cover

from typing import Any  # pragma: no cover


class OneField:
    """Class for just one field."""

    def __init__(self, name: str = "", value: Any = "") -> None:
        """One field initialization.

        :param name: field name,
        :param value: field value
        """
        self.name = name
        self.value = value

    def __str__(self) -> str:
        """:return: string representation of field."""
        return f"self.{self.name} = {self.value}"


class OneClass:
    """Class for one class."""

    indent = 2
    fill = " "

    def __init__(self, name: str = "") -> None:
        """Сlass initialization."""
        self.name = name
        self.fields: list[OneField] = list()

    def __prepare_str(self) -> str:
        lines = list()
        lines.append(f"class {self.name}:")
        if not self.fields:
            lines.append("  pass")
            return "\n".join(lines)

        lines.append(f"{self.fill * self.indent}def __init__(self):")
        for f in self.fields:
            lines.append(f"{self.fill * 2 * self.indent}{f}")

        return "\n".join(lines)

    def __str__(self) -> str:
        """Class string representation."""
        return self.__prepare_str()


class CodeBuilder:
    """Class for builder (builder pattern)."""

    def __init__(self, class_name: str) -> None:
        """Init code builder."""
        self.__class = OneClass(class_name)

    def add_field(self, name: str, value: Any) -> CodeBuilder:
        """Main method for adding new fields.

        :param name: fields name,
        :param value: field value,
        :return: class instance.
        """
        self.__class.fields.append(OneField(name, value))
        return self

    def __str__(self) -> str:
        """:return: str representation of CodeBuilder."""
        return self.__class.__str__()


def main():  # pragma: no cover
    """Main."""
    cb = CodeBuilder("Person").add_field("name", "''").add_field("age", 0)
    print(cb)


if __name__ == "__main__":  # pragma: no cover
    main()
