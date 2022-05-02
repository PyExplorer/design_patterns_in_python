"""Tests for classes with flyweight pattern."""
from src.design_patterns_in_python.chain_of_responsibility import Game
from src.design_patterns_in_python.chain_of_responsibility import Goblin
from src.design_patterns_in_python.chain_of_responsibility import GoblinKing


class TestGoblin:
    """Tests for Goblin."""

    def test_goblin(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin = Goblin("Goblin 1", game)
        assert goblin.attack == 1
        assert goblin.defense == 1


class TestGoblinKing:
    """Tests for King Goblin."""

    def test_goblin_king(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin = GoblinKing("Goblin King", game)
        assert goblin.attack == 3
        assert goblin.defense == 3


class TestGame:
    """Tests for the pattern."""

    def test_pattern(self):  # noqa: D102
        game = Game("Goblin fight")

        goblin = Goblin("Goblin 1", game)
        game.creatures.append(goblin)

        assert goblin.attack == 1
        assert goblin.defense == 1

        goblin2 = Goblin("Goblin 2", game)
        game.creatures.append(goblin2)

        assert goblin.attack == 1
        assert goblin.defense == 2

        goblin3 = GoblinKing("Goblin King", game)
        game.creatures.append(goblin3)

        assert goblin.attack == 2
        assert goblin.defense == 3
