"""Adapter - a construct which adapts an existing interface to conform to the required interface Y."""
from __future__ import annotations  # pragma: no cover


class Square:
    """Just Square class."""

    def __init__(self, side: float = 0) -> None:
        """Initialization."""
        self.side = side

    def __str__(self) -> str:
        """String representation."""
        return f"Square {self.side} x {self.side}"


def calculate_area(rc) -> float:
    """External function for rectangle square calculation."""
    return rc.width * rc.height


class SquareToRectangleAdapter:
    """Adapter for Square class for using calculate_area()."""

    def __init__(self, square: Square) -> None:
        """Initialization."""
        self.square = square

    @property
    def width(self) -> float:
        """Width."""
        return self.square.side

    @property
    def height(self) -> float:
        """Height."""
        return self.square.side

    def __str__(self) -> str:
        """String representation."""
        return f"Square adapter: {self.width} x {self.height}"


def main():  # pragma: no cover
    """Main."""
    sq = Square(20)
    adapter = SquareToRectangleAdapter(sq)
    print(calculate_area(adapter))
    sq.side = 10
    print(calculate_area(adapter))


if __name__ == "__main__":  # pragma: no cover
    main()
