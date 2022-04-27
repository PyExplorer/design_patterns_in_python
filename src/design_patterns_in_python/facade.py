"""Facade pattern.

Provides a simple , easy to understand user interface over a large and sophisticated body of code.
"""
from random import randint
from typing import List, Union


class Generator:
    """This class generates a 1-dimensional list of random digits in range 1 to 9."""

    @staticmethod
    def generate(count: int) -> List[int]:  # noqa: D102
        return [randint(1, 9) for x in range(count)]  # noqa: S311


class Splitter:
    """This class takes a 2D list and splits it into all possible arrangements of 1D lists.

    It gives you the columns, the rows and the two diagonals.
    """

    @staticmethod
    def split(array: List[List[int]]) -> List[List[int]]:  # noqa: D102
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    """This class takes a 2D list and verifies that the sum of elements in every sublist is the same."""

    @staticmethod
    def verify(arrays: Union[List[List[int]], None]) -> bool:  # noqa: D102
        if not arrays:
            return False

        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    """The class simply generates the magic square of a given size."""

    @staticmethod
    def generate(size: int, steps: int = 100) -> Union[List[List[int]], None]:  # noqa: D102
        # return a magic square of the given size
        g = Generator()
        s = Splitter()
        v = Verifier()
        step = 1
        while True and step < steps:
            gen = g.generate(size)
            d2_list = [gen for _ in range(size)]
            if v.verify(s.split(d2_list)):
                return d2_list


def main(size: int):  # noqa: D102
    msg = MagicSquareGenerator()
    print(msg.generate(size))


if __name__ == "__main__":  # pragma: no cover
    main(3)
