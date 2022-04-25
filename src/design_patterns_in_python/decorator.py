"""Decorator pattern (oop)

Facilitates the addition of behaviors to individual objects without inheriting from them
"""


class Circle:
    """Circle."""

    def __init__(self, radius: float) -> None:  # noqa: D107
        self.radius = radius

    def resize(self, factor: float) -> None:
        self.radius *= factor

    def __str__(self) -> str:  # noqa: D105
        return f"A circle of radius {self.radius}"


class Square:
    """Square."""

    def __init__(self, side: float) -> None:  # noqa: D107
        self.side = side

    def __str__(self) -> str:  # noqa: D105
        return f"A square with side {self.side}"


class ColoredShape:
    def __init__(self, shape, color: str) -> None:  # noqa: D107
        self.color = color
        self.shape = shape

    def resize(self, factor: float) -> None:
        if callable(getattr(self.shape, "resize", None)):
            self.shape.resize(factor)

    def __str__(self) -> str:  # noqa: D105
        return f"{self.shape} has the color {self.color}"


def main():  # pragma: no cover
    """Main."""
    circle = ColoredShape(Circle(5), "red")
    print(str(circle))
    square = ColoredShape(Square(2), "blue")
    square.resize(2)
    print(str(square))


if __name__ == "__main__":  # pragma: no cover
    main()
