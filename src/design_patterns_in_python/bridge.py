"""Bridge pattern - a mechanism that decouples an interface (hierarchy) from an implementation (hierarchy)."""
from abc import ABC
from abc import abstractmethod


class Renderer(ABC):
    """Abstract Renderer class."""

    @abstractmethod
    def what_to_render_as(self) -> str:
        """Abstract property for future classes."""
        return ""


class VectorRenderer(Renderer):
    """Vectors."""

    @property
    def what_to_render_as(self) -> str:  # noqa
        return "lines"


class RasterRenderer(Renderer):
    """Rasters."""

    @property
    def what_to_render_as(self) -> str:  # noqa
        return "pixels"


class Shape(ABC):
    """Abstract for Shapes."""

    def __init__(self, name, renderer) -> None:  # noqa: D107
        self.name = name
        self.renderer = renderer

    def __str__(self) -> str:  # noqa: D105
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Triangle(Shape):
    """Triangle."""

    def __init__(self, renderer) -> None:  # noqa: D107
        super().__init__("Triangle", renderer)


class Square(Shape):
    """Square."""

    def __init__(self, renderer) -> None:  # noqa: D107
        super().__init__("Square", renderer)


def main():  # pragma: no cover
    """Main."""
    print(str(Square(VectorRenderer())))
    print(str(Square(RasterRenderer())))
    print(str(Triangle(VectorRenderer())))
    print(str(Triangle(RasterRenderer())))


if __name__ == "__main__":  # pragma: no cover
    main()
