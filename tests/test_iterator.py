"""Tests for classes with iterator pattern."""

from src.design_patterns_in_python.iterator import Node


class TestIterator:
    """Tests nodes traverse."""

    def test_traverse_preorder(self):  # noqa: D102
        node = Node("a", Node("b", Node("c"), Node("d")), Node("e"))
        assert "".join([x for x in node.traverse_preorder()]) == "abcde"
