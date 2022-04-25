"""Tests for classes with decorator pattern."""
from src.design_patterns_in_python.decorator import Circle
from src.design_patterns_in_python.decorator import ColoredShape
from src.design_patterns_in_python.decorator import Square


class TestShapes:
    def test_circle(self):
        circle = ColoredShape(Circle(5), "red")
        assert str(circle) == "A circle of radius 5 has the color red"
        circle.resize(2)
        assert str(circle) == "A circle of radius 10 has the color red"

    def test_no_resize_in_square(self):
        square = Square(4)
        r = getattr(square, "resize", None)
        assert not callable(r)

    def test_square(self):
        square = ColoredShape(Square(2), "blue")
        assert str(square) == "A square with side 2 has the color blue"
        square.resize(2)
        assert str(square) == "A square with side 2 has the color blue"
