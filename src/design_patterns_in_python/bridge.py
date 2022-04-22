"""Bridge pattern - a mechanism that decouples an interface (hierarchy) from an implementation (hierarchy)."""
from abc import ABC


class Renderer(ABC):
    """Abstract Renderer class."""

    @property
    def what_to_render_as(self):
        """Abstract property for future classes."""
        return None


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
