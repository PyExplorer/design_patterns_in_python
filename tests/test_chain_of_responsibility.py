"""Tests for classes with chain of responsibility pattern."""
from src.design_patterns_in_python.chain_of_responsibility import Game
from src.design_patterns_in_python.chain_of_responsibility import Goblin
from src.design_patterns_in_python.chain_of_responsibility import GoblinKing
from src.design_patterns_in_python.chain_of_responsibility import Query
from src.design_patterns_in_python.chain_of_responsibility import WhatToQuery


class TestGoblin:
    """Tests for Goblin."""

    def test_goblin(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin = Goblin("Goblin 1", game)
        assert goblin.attack == 1
        assert goblin.defense == 1

    def test_str_goblin(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin = Goblin("Goblin 1", game)
        assert str(goblin) == (
            "Goblin 1 in (Game: Goblin fight with number of creatures: 0) with attack: 1 and defence: 1"
        )

    def test_query(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin_1 = Goblin("Goblin 1", game)
        goblin_2 = Goblin("Goblin 2", game)
        query = Query(1, WhatToQuery.DEFENSE)
        assert query.value == 1
        goblin_1.query(goblin_2, query)
        assert query.value == 2


class TestGoblinKing:
    """Tests for King Goblin."""

    def test_goblin_king(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin = GoblinKing("Goblin King", game)
        assert goblin.attack == 3
        assert goblin.defense == 3

    def test_query_increasing(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin_1 = GoblinKing("Goblin King", game)
        goblin_2 = Goblin("Goblin 2", game)
        query = Query(1, WhatToQuery.ATTACK)
        assert query.value == 1
        goblin_1.query(goblin_2, query)
        assert query.value == 2

    def test_query_no_change(self):  # noqa: D102
        game = Game("Goblin fight")
        goblin_1 = GoblinKing("Goblin King", game)
        query = Query(1, WhatToQuery.DEFENSE)
        assert query.value == 1
        goblin_1.query(goblin_1, query)
        assert query.value == 1


class TestGame:
    """Tests for the pattern."""

    def test_empty_game(self):  # noqa: D102
        game = Game("Goblin fight")
        assert str(game) == "(Game: Goblin fight with number of creatures: 0)"

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
