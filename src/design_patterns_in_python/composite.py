"""Composite pattern.

A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.
"""
from abc import ABC
from abc import abstractmethod
from collections.abc import Iterable
from typing import Iterator


class BaseValue(Iterable, ABC):
    """Base class for composite."""

    value_name = ""

    @property
    def sum(self) -> float:
        """Sum over the objects."""
        result = 0
        for value in self:
            if not (isinstance(value, BaseValue)):
                result += value
                continue

            for i in value:
                result += i
        return result

    @property
    def name(self) -> str:  # noqa: D102
        return self.value_name


class SingleValue(BaseValue):
    """Single value."""

    value_name = "Single value"

    def __init__(self, value) -> None:  # noqa: D107
        self.value = value

    def __iter__(self) -> Iterator[float]:  # noqa: D105
        yield self.value

    def __str__(self) -> str:  # noqa: D105
        return f"{self.value_name}: {self.value}"


class ManyValues(list, BaseValue):
    """Many values."""

    value_name = "Many values"

    def __str__(self) -> str:  # noqa: D105
        return f"{self.value_name}: {', '.join(map(str, self))}"


def main():  # pragma: no cover
    """Main."""
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)

    print(str(single_value), str(other_values), str(all_values), sep="\n")
    print("Sum: ", single_value.sum, other_values.sum, all_values.sum)


if __name__ == "__main__":  # pragma: no cover
    main()
