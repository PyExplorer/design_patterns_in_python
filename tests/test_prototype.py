"""Tests for classes with prototype pattern."""
import pytest
from src.design_patterns_in_python.prototype import Line
from src.design_patterns_in_python.prototype import Point


class TestPoint:
    """Test case for one field."""

    def test_point_init(self) -> None:
        """Test case for point initialization."""
        assert str(Point(1.23, 2.33)) == f"x: {1.23}, y: {2.33}"


class TestLine:
    """Test case for Line."""

    @pytest.mark.parametrize(
        "start, end, expected",
        [
            pytest.param(Point(1, 3), Point(5, 7), "start: x: 1, y: 3, end: x: 5, y: 7"),
            pytest.param(None, None, "start: x: 0, y: 0, end: x: 0, y: 0"),
            pytest.param(Point(1, 3), None, "start: x: 1, y: 3, end: x: 0, y: 0"),
            pytest.param(None, Point(5, 7), "start: x: 0, y: 0, end: x: 5, y: 7"),
        ],
    )
    def test_init(self, start, end, expected) -> None:
        """Test init."""
        assert str(Line(start, end)) == expected

    def test_line(self) -> None:
        """Testing deepcopy for line."""
        line1 = Line(Point(1, 3), Point(5, 7))
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0
        assert line2.start.x == 1
        assert line2.start.y == 3
        assert line2.end.x == 5
        assert line2.end.y == 7
