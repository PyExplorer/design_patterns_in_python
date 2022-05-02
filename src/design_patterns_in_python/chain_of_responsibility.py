"""Chain fo responsibility

A chain of components who all get a chance to process a command or a query,
optionally having default processing implementation and an ability to terminate
the processing chain.
"""
from __future__ import annotations  # pragma: no cover

from abc import ABC
from abc import abstractmethod
from enum import Enum


class WhatToQuery(Enum):
    """Actions enumerator."""

    ATTACK = 1
    DEFENSE = 2


class Creature(ABC):
    """Abstract for creatures"""

    def __init__(self, name: str, game: Game, attack: int, defense: int) -> None:  # noqa: D107
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game
        self.name = name

    def __str__(self) -> str:  # noqa: D105
        return f"{self.name} in {self.game} with attack: {self.attack} and defence: {self.defense}"

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass

    def query(self, source, query):
        pass


class Goblin(Creature):
    """Simple Goblin."""

    def __init__(self, name: str, game: Game, attack: int = 1, defense: int = 1) -> None:  # noqa: D107
        super().__init__(name, game, attack, defense)

    @property
    def attack(self) -> int:  # noqa: D102
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self) -> int:  # noqa: D102
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source: Goblin, query: Query) -> None:  # noqa: D102:
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    """King Goblin."""

    def __init__(self, name: str, game: Game, attack: int = 3, defense: int = 3) -> None:  # noqa: D107
        super().__init__(name, game, attack, defense)

    def query(self, source: Goblin, query: Query) -> None:  # noqa: D102:
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class Query:
    """Query."""

    def __init__(self, initial_value: int, what_to_query: WhatToQuery) -> None:  # noqa: D107
        self.what_to_query = what_to_query
        self.value = initial_value


class Game:
    """Game."""

    def __init__(self, name: str) -> None:  # noqa: D107
        self.creatures: list[Creature] = list()
        self.name = name

    def __str__(self) -> str:  # noqa: D105
        return f"(Game: {self.name} with number of creatures: {len(self.creatures)})"


def main():  # noqa: D103, pragma: no cover
    """
    1. A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.
    2. When the Goblin King is in play, every other goblin gets +1 Attack.
    3. Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).
    """
    game = Game("Goblin fight")

    goblin = Goblin("Goblin 1", game)
    game.creatures.append(goblin)
    print(*game.creatures, sep="\n")
    print()

    goblin2 = Goblin("Goblin 2", game)
    game.creatures.append(goblin2)

    print(*game.creatures, sep="\n")
    print()

    goblin3 = GoblinKing("Goblin 3", game)
    game.creatures.append(goblin3)

    print(*game.creatures, sep="\n")


if __name__ == "__main__":  # pragma: no cover
    main()
