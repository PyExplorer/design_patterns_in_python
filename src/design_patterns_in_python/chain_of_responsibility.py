"""Chain fo responsibility

A chain of components who all get a chance to process a command or a query,
optionally having default processing implementation and an ability to terminate
the processing chain.
"""

from abc import ABC
from enum import Enum
from abc import abstractmethod


class Creature(ABC):
    def __init__(self, name, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game
        self.name = name

    def __str__(self):
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
    def __init__(self, name, game, attack=1, defense=1):
        super().__init__(name, game, attack, defense)

    @property
    def attack(self):
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, name, game):
        super().__init__(name, game, attack=3, defense=3)

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, initial_value, what_to_query):
        self.what_to_query = what_to_query
        self.value = initial_value


class Game:
    def __init__(self, name):
        self.creatures = []
        self.name = name

    def __str__(self):
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
