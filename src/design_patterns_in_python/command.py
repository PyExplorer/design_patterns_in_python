"""Command pattern.

An object which represents instruction to perform a particular action.
Contains all the information necessary for the action to be taken.
"""
from __future__ import annotations  # pragma: no cover

from enum import Enum


class Action(Enum):
    """Actions enumerator."""

    DEPOSIT = 0
    WITHDRAW = 1
    NOT_SUPPORTED = 2


class Command:
    """Single command."""

    def __init__(self, action: Action, amount: float) -> None:  # noqa: D107
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    """Account."""

    def __init__(self, balance: float = 0) -> None:  # noqa: D107
        self.balance = balance
        self.last_command = False

    def process(self, command: Command) -> None:  # noqa: D102
        if command.action == Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount
        self.last_command = command.success

    def __str__(self) -> str:  # noqa: D105
        return f"Balance: {self.balance}, last command was successful: {self.last_command}"


def main():  # noqa: D103, pragma: no cover
    """Task.

    Implement the method to process different account commands with rules:
    1. Success indicates whether the operation was successful
    2.You can only withdraw money if you have enough in your account
    """
    a = Account()

    cmd = Command(Action.DEPOSIT, 100)
    a.process(cmd)
    print(a)

    cmd = Command(Action.WITHDRAW, 50)
    a.process(cmd)
    print(a)

    cmd.amount = 150
    a.process(cmd)
    print(a)


if __name__ == "__main__":  # pragma: no cover
    main()
