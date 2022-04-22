"""Tests for classes with bridge pattern."""
from src.design_patterns_in_python.bridge import RasterRenderer
from src.design_patterns_in_python.bridge import Square
from src.design_patterns_in_python.bridge import Triangle
from src.design_patterns_in_python.bridge import VectorRenderer


class TestShapes:
    """Test case for shapes."""

    def test_square_vector(self) -> None:
        """Test case for square as vector."""
        sq = Square(VectorRenderer())
        assert str(sq) == "Drawing Square as lines"

    def test_square_pixels(self) -> None:
        """Test case for square as raster."""
        sq = Square(RasterRenderer())
        assert str(sq) == "Drawing Square as pixels"

    def test_triangle_vector(self) -> None:
        """Test case for triangle as vector."""
        sq = Triangle(VectorRenderer())
        assert str(sq) == "Drawing Triangle as lines"

    def test_triangle_pixels(self) -> None:
        """Test case for square as raster."""
        sq = Triangle(RasterRenderer())
        assert str(sq) == "Drawing Triangle as pixels"
