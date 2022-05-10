"""Interpreter pattern.

A component that processes a structured data text data. Does so by turning it into
separate lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).
"""


import re
from enum import Enum


class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = "/"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def re(cls):
        return re.escape("".join(Operator.list()))

class ExpressionProcessor:
    operations = {
        Operator.PLUS: lambda x, y: x + y,
        Operator.MINUS: lambda x, y: x - y,
        Operator.MULT: lambda x, y: x * y,
        Operator.DIV: lambda x, y: x / y,
        None: lambda _, y: y
    }

    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        current = 0
        operator = None

        for part in re.split(rf"(?<=[{Operator.re()}])", expression):
            op = re.split(rf"[{Operator.re()}]", part)
            first = op[0]
            try:
                value = float(first)
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
    """Task."""

    ep = ExpressionProcessor()
    ep.variables["x"] = 5
    print(ep.calculate("1+2"))
    print(ep.calculate("1+2+x"))
    print(ep.calculate("1*2+x"))
    print(ep.calculate("6/2*x+6"))


if __name__ == "__main__":  # pragma: no cover
    main()
