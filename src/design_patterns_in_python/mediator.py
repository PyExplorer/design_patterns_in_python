"""Mediator.

A component that facilitates communication between other components without them necessarily
being aware of each other or having direct (reference) access to each other.
Mediator has functions the components can call
Components have functions the mediator can call
"""
from __future__ import annotations  # pragma: no cover


class Events(list):
    """Class for single event."""

    def __call__(self, *args, **kwargs):  # noqa: D102
        for item in self:
            item(*args, **kwargs)


class Participant:
    """Participant."""

    def __init__(self, name: str, mediator: Mediator) -> None:  # noqa: D107
        self.value = 0
        self.mediator = mediator
        self.name = name
        mediator.events.append(self.say_event_fire)

    def say_event_fire(self, participant: Participant, value: int) -> None:  # noqa: D102
        if participant != self:
            self.value += value

    def say(self, value: int) -> None:  # noqa: D102
        print(f"{self.name} says: {value}")
        self.mediator.broadcast(self, value)

    def __str__(self) -> str:  # noqa: D105
        return f"Value is {self.value} for mediator {self.name}"


class Mediator:
    """Mediator."""

    def __init__(self):  # noqa: D107
        self.events = Events()

    def broadcast(self, participant, value):  # noqa: D102
        self.events(participant, value)


def main():  # noqa: D103, pragma: no cover
    m = Mediator()
    p1 = Participant("P1", m)
    p2 = Participant("P2", m)
    print(p1)
    print(p2)
    p1.say(2)

    print(p1)
    print(p2)

    p2.say(4)
    print(p1)
    print(p2)


if __name__ == "__main__":  # pragma: no cover
    main()
