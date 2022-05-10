"""Interpreter pattern.

A component that processes a structured data text data. Does so by turning it into
separate lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).
"""
import re
from enum import Enum


class Operator(Enum):
    """Operators enumerator."""

    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = "/"

    @classmethod
    def list(cls) -> list:  # noqa: D102
        return list(map(lambda c: c.value, cls))  # type: ignore

    @classmethod
    def re(cls) -> str:  # noqa: D102
        return re.escape("".join(Operator.list()))


class ExpressionProcessor:
    """Class for calculating expressions."""

    operations = {
        Operator.PLUS: lambda x, y: x + y,
        Operator.MINUS: lambda x, y: x - y,
        Operator.MULT: lambda x, y: x * y,
        Operator.DIV: lambda x, y: x / y,
        None: lambda _, y: y,
    }

    def __init__(self) -> None:  # noqa: D107
        self.variables: dict = {}

    def calculate(self, expression: str) -> int:  # noqa: D102
        current = 0
        operator = None

        for part in re.split(rf"(?<=[{Operator.re()}])", expression):
            op = re.split(rf"[{Operator.re()}]", part)
            first = op[0]
            try:
                value = int(first)
            except ValueError:
                if len(first) == 1 and first[0] in self.variables:
                    value = self.variables[first[0]]
                else:
                    return 0

            current = self.operations[operator](current, value)

            if part[-1] in Operator.list():
                operator = Operator(part[-1])

        return current


def main():  # noqa: D103, pragma: no cover
    """Task.

    1. Expressions use integral values (e.g., '13')  ), single-letter variables defined in Variables,
    as well as + and - operators only
    2. There is no need to support braces or any other operations
    3. If a variable is not found in variables   (or if we encounter a variable with >1 letter, e.g. ab),
    the evaluator returns 0 (zero)
    4. In case of any parsing failure, evaluator returns 0
    """
    ep = ExpressionProcessor()
    ep.variables["x"] = 5
    print(ep.calculate("1+2"))
    print(ep.calculate("1+2+x"))
    print(ep.calculate("1*2+x"))
    print(ep.calculate("6/2*x+6"))


if __name__ == "__main__":  # pragma: no cover
    main()
