"""Tests for classes with flyweight pattern."""
import pytest
from src.design_patterns_in_python.flyweight import Sentence


class TestSentence:
    """Tests."""

    def test_sentence(self):  # noqa: D102
        s = Sentence("test for the sentence")
        s[1].capitalize = True
        s[2].capitalize = True
        assert str(s) == "test FOR THE sentence"

    def test_iter_sentence(self):  # noqa: D102
        s = Sentence("test for the sentence")
        i = iter(s)
        assert next(i) == "test"
        assert next(i) == "for"

    def test_stop_iter_sentence(self):  # noqa: D102
        s = Sentence("stop iter")
        i = iter(s)
        next(i)
        next(i)
        with pytest.raises(StopIteration):
            next(i)
