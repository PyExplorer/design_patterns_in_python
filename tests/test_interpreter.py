"""Tests for classes with interpreter pattern."""
from src.design_patterns_in_python.interpreter import Operator
from src.design_patterns_in_python.interpreter import ExpressionProcessor
import pytest

class TestExpressionProcessor:
    @pytest.mark.parametrize(
        "test, expected",
        [
            pytest.param("1+2", 3),
            pytest.param("1+2+3", 6),
            pytest.param("2-1", 1),
            pytest.param("24-1-10", 13),
            pytest.param("24-1+2", 25),
            pytest.param("24*2+2-15", 35),
            pytest.param("24/2+2-15", -1),
            pytest.param("24/2/2-1+4", 9),
        ],
    )
    def test_int_calculator(self, test, expected):
        ep = ExpressionProcessor()
        assert ep.calculate(test) == expected

    @pytest.mark.parametrize(
        "test, expected",
        [
            pytest.param("10*x+2*x-3*x+x/5", 258),
            pytest.param("x/x*x+x-x", 5),

        ],
    )
    def test_one_variable_calculator(self, test, expected):
        ep = ExpressionProcessor()
        ep.variables["x"] = 5
        assert ep.calculate(test) == expected

    @pytest.mark.parametrize(
        "test, expected",
        [
            pytest.param("10*x+2*y-3*y+x/2", 206),
            pytest.param("x/y*x+y-x", 42),

        ],
    )
    def test_multiple_variable_calculator(self, test, expected):
        ep = ExpressionProcessor()
        ep.variables["x"] = 10
        ep.variables["y"] = 2
        assert ep.calculate(test) == expected
