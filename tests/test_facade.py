"""Tests for classes with facade pattern."""
import pytest
from src.design_patterns_in_python.facade import Generator
from src.design_patterns_in_python.facade import MagicSquareGenerator
from src.design_patterns_in_python.facade import Splitter
from src.design_patterns_in_python.facade import Verifier


class TestMagicSquareGenerator:
    def test_magic_square_generator(self):  # noqa: D102
        assert Verifier().verify(MagicSquareGenerator().generate(3))


class TestGenerator:
    def test_generate(self):  # noqa: D102
        assert len(Generator.generate(5)) == 5


class TestSplitter:
    def test_split(self):  # noqa: D102
        inp = [[5, 7, 1], [5, 7, 1], [5, 7, 1]]
        out = [
            [5, 7, 1],
            [5, 7, 1],
            [5, 7, 1],
            [5, 7, 1],
            [5, 7, 1],
            [5, 7, 1],
            [5, 5, 5],
            [7, 7, 7],
            [1, 1, 1],
            [5, 7, 1],
            [5, 7, 1],
        ]
        assert not [x for x in out if x not in Splitter.split(inp)]


@pytest.mark.parametrize(
    "inp, expected",
    [
        pytest.param([[7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]], True),
        pytest.param([[1, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]], False),
    ],
)
class TestVerifier:
    def test_verify(self, inp, expected):
        assert Verifier.verify(inp) == expected
