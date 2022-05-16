"""Template.

Allows us to define the 'skeleton' of the algorithm, with concrete implementations defined in subclasses.
"""
from __future__ import annotations  # pragma: no cover

from abc import ABC


class Creature:
    """One Creature."""

    def __init__(self, attack: int, health: int) -> None:  # noqa: D107
        self.health = health
        self.attack = attack

    @property
    def alive(self):  # noqa: D102
        return self.health > 0


class CardGame(ABC):
    """Card Game."""

    def __init__(self, creatures) -> None:  # noqa: D107
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index: int, c2_index: int):  # noqa: D102
        first = self.creatures[c1_index]
        second = self.creatures[c2_index]
        self.hit(first, second)
        self.hit(second, first)

        if first.alive and second.alive:
            return -1

        if not first.alive and not second.alive:
            return -1

        return c1_index if first.alive else c2_index

    def hit(self, attacker, defender):  # noqa: D102, pragma: no cover
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    """TemporaryDamageCardGame.

    In some games, unless the creature has been killed,
    its health returns to the original value at the end of combat.
    """

    def hit(self, attacker, defender):  # noqa: D102
        if defender.health - attacker.attack <= 0:
            defender.health = 0


class PermanentDamageCardGame(CardGame):
    """PermanentDamageCardGame.

    In other games, health damage persists.
    """

    def hit(self, attacker, defender):  # noqa: D102
        defender.health -= attacker.attack


def main():  # noqa: D103, pragma: no cover
    c1 = Creature(1, 2)
    c2 = Creature(1, 3)
    print(c1.health, c2.health)
    game = PermanentDamageCardGame([c1, c2])
    print(game.combat(0, 1))
    print(c1.health, c2.health)
    print(game.combat(0, 1))


if __name__ == "__main__":  # pragma: no cover
    main()
