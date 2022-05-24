"""Memento.

A token/handle representing the system state.
Lets us roll back to the state when the token was generated.
May or may not directly expose state information.
"""
from __future__ import annotations  # pragma: no cover

from copy import deepcopy


class Token:
    """Single Token."""

    __slots__ = ["value"]

    def __init__(self, value: float = 0) -> None:  # noqa: D107
        self.value = value


class Memento(list):
    """Just a list."""

    pass


class TokenMachine:
    """Token machine."""

    def __init__(self) -> None:  # noqa: D107
        self.tokens: list[float] = []

    def add_token_value(self, value: float) -> Memento:  # noqa: D102
        return self.add_token(Token(value))

    def add_token(self, token: Token) -> Memento:  # noqa: D102
        self.tokens.append(token)
        dc = deepcopy(self.tokens)
        return Memento(dc)

    def revert(self, memento: Memento) -> None:  # noqa: D102
        self.tokens = [Token(x.value) for x in memento]


def main():  # noqa: D103, pragma: no cover
    tm = TokenMachine()
    tm.add_token_value(1)
    m = tm.add_token_value(2)
    tm.add_token_value(3)
    tm.revert(m)
    print(len(tm.tokens))
    print(tm.tokens[0].value)
    print(tm.tokens[1].value)


if __name__ == "__main__":  # pragma: no cover
    main()
