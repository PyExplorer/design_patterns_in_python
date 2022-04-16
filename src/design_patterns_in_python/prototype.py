"""Prototype pattern."""
from __future__ import annotations  # pragma: no cover


class Point:
    """Point class."""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Initialization of the point."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """String representation for the class."""
        return f"x: {self.x}, y: {self.y}"


class Line:
    """Line class."""

    def __init__(self, start: Point = None, end: Point = None) -> None:
        """Initialization of the line."""
        if not start:
            start = Point()
        if not end:
            end = Point()

        self.start = start
        self.end = end

    def __str__(self) -> str:
        """String representation for the class."""
        return f"start: {self.start}, end: {self.end}"

    def deep_copy(self) -> Line:
        """Return a new instance of Line object as a deepcopy of existing one.

        It can be done as
        'return Line(start=deepcopy(self.start), end=deepcopy(self.end))'
        but for this exercise we don't use copy.deepcopy method
        """
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)
