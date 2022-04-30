"""Flyweight pattern.

A space optimization technique that lets us use less memory by storing external data associated with similar objects.
"""
from __future__ import annotations  # pragma: no cover


class WordFormat:
    """Class for storing formats"""

    def __init__(self, capitalize: bool = False) -> None:  # noqa: D107
        self.capitalize = capitalize


class Sentence:
    """One sentence."""

    def __init__(self, plain_text: str) -> None:  # noqa: D107
        self.words = plain_text.split(" ")
        self.formats = {}

    def __iter__(self) -> Sentence:  # noqa: D107:
        self.current = 0
        return self

    def __next__(self) -> str:  # noqa: D107
        if self.current < len(self.words):
            self.current += 1
            return self.words[self.current - 1]
        else:
            raise StopIteration

    def __getitem__(self, index: int) -> WordFormat:  # noqa: D107
        wf = WordFormat()
        self.formats[index] = wf
        return self.formats[index]

    def __str__(self) -> str:  # noqa: D107
        result = []
        for i, word in enumerate(self.words):
            if i in self.formats and self.formats[i].capitalize:
                word = word.upper()
            result.append(word)

        return " ".join(result)


def main():  # noqa: D103
    sentence = Sentence("Hello unexplored world")  # pragma: no cover
    print(*sentence)
    sentence[1].capitalize = True  # pragma: no cover
    print(sentence)


if __name__ == "__main__":  # pragma: no cover
    main()
