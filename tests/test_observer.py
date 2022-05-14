"""Tests for classes with observer pattern."""
from src.design_patterns_in_python.observer import Game
from src.design_patterns_in_python.observer import Rat

from unittest import TestCase


class Evaluate(TestCase):
    """Tests for Observer."""
    def test_single_rat(self):  # noqa: D102
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):  # noqa: D102
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):  # noqa: D102
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)
