"""Visitor.

A component (visitor) that knows how to traverse a data structure composed
of (possibly related) types.
"""
# taken from https://tavianator.com/the-visitor-pattern-in-python/
from __future__ import annotations  # pragma: no cover

from typing import Any


def _qualname(obj: Any) -> str:
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj: object) -> str:
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[: name.rfind(".")]


# Stores the actual visitor methods
_methods: dict[Any, Any] = dict()


# Delegating visitor implementation
def _visitor_impl(self, arg: Any) -> Any:
    """Actual visitor method implementation."""
    key = (_qualname(type(self)), type(arg))
    if key not in _methods:
        raise Exception(f"Key {key} not found")
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type: Any) -> Any:
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class Value:
    """Value."""

    __slots__ = ["value"]

    def __init__(self, value: float):  # noqa: D107
        self.value = value


class AdditionExpression:
    """Simple addition."""

    __slots__ = ["right", "left"]

    def __init__(self, left: Value, right: Value):  # noqa: D107
        self.right = right
        self.left = left


class MultiplicationExpression:
    """Multiplication."""

    def __init__(self, left: AdditionExpression | Value, right: AdditionExpression | Value):  # noqa: D107
        self.right = right
        self.left = left


class ExpressionPrinter:
    """Output for expression."""

    __slots__ = ["buffer"]

    def __init__(self):  # noqa: D107
        self.buffer = []

    @visitor(Value)
    def visit(self, e: Value) -> None:  # noqa: D102, F811
        self.buffer.append(str(e.value))

    @visitor(AdditionExpression)
    def visit(self, e: AdditionExpression) -> None:  # noqa: D102
        self.buffer.append("(")
        self.visit(e.left)
        self.buffer.append("+")
        self.visit(e.right)
        self.buffer.append(")")

    @visitor(MultiplicationExpression)
    def visit(self, e: MultiplicationExpression) -> None:  # noqa: D102, F811
        self.visit(e.left)
        self.buffer.append("*")
        self.visit(e.right)

    def __str__(self) -> str:  # noqa: D105
        return "".join(self.buffer)


def main():  # noqa: D103, pragma: no cover
    simple = AdditionExpression(Value(2), Value(3))
    ep = ExpressionPrinter()
    ep.visit(simple)
    print(str(ep))

    expr = MultiplicationExpression(AdditionExpression(Value(2), Value(3)), Value(4))
    ep = ExpressionPrinter()
    ep.visit(expr)
    print(str(ep))


if __name__ == "__main__":  # pragma: no cover
    main()
