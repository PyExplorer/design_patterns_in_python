"""Tests for classes with adapter pattern."""
from src.design_patterns_in_python.adapter import calculate_area
from src.design_patterns_in_python.adapter import Square
from src.design_patterns_in_python.adapter import SquareToRectangleAdapter


class Rect:
    """Class for rectangle."""

    __slots__ = "height", "width"

    def __init__(self, width: float = 0, height: float = 0) -> None:
        """Rectangle init."""
        self.height = height
        self.width = width


class TestSquare:
    """Test for Square class."""

    def test_init_default(self) -> None:
        """Default init."""
        square = Square()
        assert str(square) == "Square 0 x 0"

    def test_init(self) -> None:
        """Init with value."""
        square = Square(10)
        assert str(square) == "Square 10 x 10"


class TestSquareToRectangleAdapter:
    """Test for adapter."""

    def test_init(self) -> None:
        """Default init."""
        adapter = SquareToRectangleAdapter(Square(4))
        assert str(adapter) == "Square adapter: 4 x 4"

    def test_adapter(self) -> None:
        """Test how adapter works."""
        sq = Square(20)
        adapter = SquareToRectangleAdapter(sq)
        assert calculate_area(adapter) == 400
        sq.side = 10
        assert calculate_area(adapter) == 100


def test_calculate_area() -> None:
    """Area calculation."""
    assert calculate_area(Rect(5, 3)) == 15
