"""Tests for classes with adapter pattern."""
from src.design_patterns_in_python.adapter import calculate_area
from src.design_patterns_in_python.adapter import Square
from src.design_patterns_in_python.adapter import SquareToRectangleAdapter


class Rect:
    def __init__(self, width: float = 0, height: float = 0):
        self.height = height
        self.width = width


class TestSquare:
    def test_init_default(self):
        square = Square()
        assert str(square) == "Square 0 x 0"

    def test_init(self):
        square = Square(10)
        assert str(square) == "Square 10 x 10"


class TestSquareToRectangleAdapter:
    def test_init(self):
        adapter = SquareToRectangleAdapter(Square(4))
        assert str(adapter) == "Square adapter: 4 x 4"

    def test_adapter(self):
        sq = Square(20)
        adapter = SquareToRectangleAdapter(sq)
        assert calculate_area(adapter) == 400
        sq.side = 10
        assert calculate_area(adapter) == 100


def test_calculate_area():
    assert calculate_area(Rect(5, 3)) == 15
