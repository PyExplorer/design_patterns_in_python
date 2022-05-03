"""Command pattern.

An object which represents instruction to perform a particular action.
Contains all the information necessary for the action to be taken.
"""
from __future__ import annotations  # pragma: no cover

from enum import Enum


class Command:
    class Action(Enum):
        """Actions enumerator."""
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount
