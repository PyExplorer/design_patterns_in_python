"""Iterator pattern.

An object that facilitates the traversal of data structure.
"""
from __future__ import annotations  # pragma: no cover

from typing import Generator


class Node:
    """Class for Node."""

    def __init__(self, value: str, left: Node = None, right: Node = None) -> None:  # noqa: D107
        self.right = right
        self.left = left
        self.value = value
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def traverse_preorder(self) -> Generator[str, None, None]:  # noqa: D102
        yield self.value
        if self.left:
            yield from self.left.traverse_preorder()
        if self.right:
            yield from self.right.traverse_preorder()


def main():  # noqa: D103, pragma: no cover
    """Task.

    Given the following definition of a Node, please implement preorder traversal  right inside Node.
    The sequence returned should be the sequence of values, not their containing nodes.
    """
    node = Node("a", Node("b", Node("c"), Node("d")), Node("e"))
    print("".join([x for x in node.traverse_preorder()]))


if __name__ == "__main__":  # pragma: no cover
    main()
