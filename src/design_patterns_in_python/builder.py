from __future__ import annotations

from typing import Any


class OneField:
    """
    Class for just one field
    """

    indent_size = 2

    def __init__(self, name: str = "", value: Any = "") -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"self.{self.name} = {self.value}"


class OneClass:
    """
    Class for one class
    """

    indent = 2
    fill = " "

    def __init__(self, name: str = "") -> None:
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
        return self.__prepare_str()


class CodeBuilder:
    """
    Class for builder (builder pattern)
    """

    def __init__(self, class_name: str) -> None:
        self.__class = OneClass(class_name)

    def add_field(self, name: str, value: Any) -> CodeBuilder:
        self.__class.fields.append(OneField(name, value))
        return self

    def __str__(self) -> str:
        return self.__class.__str__()


cb = CodeBuilder("Person").add_field("name", "''").add_field("age", 0)

print(cb)
