"""Tests for classes with Visitor pattern."""
from unittest import TestCase

from src.design_patterns_in_python.visitor import AdditionExpression
from src.design_patterns_in_python.visitor import ExpressionPrinter
from src.design_patterns_in_python.visitor import MultiplicationExpression
from src.design_patterns_in_python.visitor import Value


class Evaluate(TestCase):
    """Test."""

    def test_simple_addition(self):  # noqa: D102
        simple = AdditionExpression(Value(2), Value(3))
        ep = ExpressionPrinter()
        ep.visit(simple)
        self.assertEqual("(2+3)", str(ep))

    def test_product_of_addition_and_value(self):  # noqa: D102
        expr = MultiplicationExpression(AdditionExpression(Value(2), Value(3)), Value(4))
        ep = ExpressionPrinter()
        ep.visit(expr)
        self.assertEqual("(2+3)*4", str(ep))
