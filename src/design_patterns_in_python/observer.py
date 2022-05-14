"""Observer.

An observer is an object that wishes to be informed about events happening in the system.
The entity generating the events is an observable.
"""
from __future__ import annotations  # pragma: no cover

from typing import Any


class Event(list):
    """Event's list."""

    def __call__(self, *args, **kwargs):  # noqa: D102
        for item in self:
            item(*args, **kwargs)


class Game:
    """Game."""

    def __init__(self) -> None:  # noqa: D107
        self.rat_enters = Event()
        self.rat_leaves = Event()
        self.rat_broadcast = Event()


class Rat:
    """Rat."""

    __slots__ = ["attack", "game"]

    def __init__(self, game: Game) -> None:  # noqa: D107
        self.game = game
        self.attack = 1

        self.game.rat_enters.append(self.enters)
        self.game.rat_leaves.append(self.leaves)
        self.game.rat_broadcast.append(self.broadcast)

        self.game.rat_enters(self)

    def __enter__(self) -> Rat:  # noqa: D105
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:  # noqa: D105
        self.game.rat_leaves(self)

    def enters(self, rat: Rat) -> None:  # noqa: D102
        if rat != self:
            self.attack += 1
            self.game.rat_broadcast(rat)

    def broadcast(self, rat: Rat) -> None:  # noqa: D102
        if rat == self:
            self.attack += 1

    def leaves(self, rat: Rat = None) -> None:  # noqa: D102
        self.attack -= 1


def main():  # noqa: D103, pragma: no cover
    """Task.

    Imagine a game where one or more rats can attack a player.
    Each individual rat has an initial attack value of 1.
    However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.
    Given that a rat enters play through the initializer and leaves play (dies) via its __exit__  method,
    please implement the Game and Rat classes so that, at any point in the game,
    the Attack value of a rat is always consistent.
    """
    game = Game()
    rat = Rat(game)
    print(rat.attack)
    rat2 = Rat(game)
    print(rat.attack, rat2.attack)


if __name__ == "__main__":  # pragma: no cover
    main()
