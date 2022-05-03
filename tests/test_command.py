"""Tests for classes with command pattern."""
from src.design_patterns_in_python.command import Account
from src.design_patterns_in_python.command import Action
from src.design_patterns_in_python.command import Command


class TestAccount:
    """Tests for Account."""

    def test_deposit(self):  # noqa: D102
        a = Account()
        cmd = Command(Action.DEPOSIT, 100)
        a.process(cmd)
        assert a.balance == 100

    def test_withdraw(self):  # noqa: D102
        a = Account()
        cmd = Command(Action.DEPOSIT, 100)
        a.process(cmd)
        cmd = Command(Action.WITHDRAW, 30)
        a.process(cmd)
        assert a.balance == 70

    def test_failed_withdraw(self):  # noqa: D102
        a = Account()
        cmd = Command(Action.DEPOSIT, 100)
        a.process(cmd)
        cmd = Command(Action.WITHDRAW, 300)
        a.process(cmd)
        assert a.balance == 100

    def test_str(self):  # noqa: D102
        a = Account()
        cmd = Command(Action.DEPOSIT, 100)
        a.process(cmd)
        assert str(a) == "Balance: 100, last command was successful: True"

    def test_wrong_actions(self):  # noqa: D102
        a = Account()
        cmd = Command(Action.NOT_SUPPORTED, 100)
        a.process(cmd)
        assert str(a) == "Balance: 0, last command was successful: False"
