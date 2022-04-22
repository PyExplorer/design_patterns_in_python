"""Tests for classes with bridge pattern."""
import pytest
from src.design_patterns_in_python.bridge import RasterRenderer
from src.design_patterns_in_python.bridge import Renderer
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
        tr = Triangle(VectorRenderer())
        assert str(tr) == "Drawing Triangle as lines"

    def test_triangle_pixels(self) -> None:
        """Test case for square as raster."""
        tr = Triangle(RasterRenderer())
        assert str(tr) == "Drawing Triangle as pixels"


class TestRasters:
    """Test case for renderer."""

    def test_raster(self) -> None:
        """Test case for raster."""
        assert RasterRenderer().what_to_render_as == "pixels"

    def test_vector(self) -> None:
        """Test case for vector."""
        assert VectorRenderer().what_to_render_as == "lines"

    def test_abc(self) -> None:
        """Test abstract raster class."""
        with pytest.raises(TypeError):
            _ = Renderer().what_to_render_as
