"""State.

The pattern in which the object's behavior is determined by its state.
An object transitions from one state to another (something needs to trigger a transition).
A formalized construct which manages state and transitions is called a state machine.
"""


class CombinationLock:
    """State pattern."""

    __slots__ = ["status", "correct_combination", "current_digit"]

    def __init__(self, combination: list) -> None:  # noqa: D107
        self.status = "LOCKED"
        self.correct_combination = combination
        self.current_digit = 0

    def is_digit_correct(self, digit: int):  # noqa: D102
        return digit == self.correct_combination[self.current_digit]

    def is_final_digit(self):  # noqa: D102
        return self.current_digit == len(self.correct_combination) - 1

    def update_status(self, digit: int):  # noqa: D102
        if self.status == "LOCKED":
            return str(digit)
        return self.status + str(digit)

    def enter_digit(self, digit: int):  # noqa: D102
        if self.is_digit_correct(digit):
            if self.is_final_digit():
                self.status = "OPEN"
                return
            self.status = self.update_status(digit)
            self.current_digit += 1

        else:
            self.status = "ERROR"


def main():  # noqa: D103, pragma: no cover
    """Task.

    A combination lock is a lock that opens after the right digits have been entered.
    A lock is pre-programmed with a combination (e.g., 12345  ) and the user is expected to enter
    this combination to unlock the lock. The lock has a Status field that indicates the state of the lock.
    The rules are:
    1. If the lock has just been locked (or at startup), the status is LOCKED.
    2. If a digit has been entered, that digit is shown on the screen.
    3. As the user enters more digits, they are added to Status.
    4. If the user has entered the correct sequence of digits, the lock status changes to OPEN.
    5. If the user enters an incorrect sequence of digits, the lock status changes to ERROR.
    Please implement the CombinationLock class to enable this behavior.
    Be sure to test both correct and incorrect inputs.
    """
    cl = CombinationLock([1, 2, 3])
    print(cl.status)
    cl.enter_digit(1)
    print(cl.status)
    cl.enter_digit(2)
    print(cl.status)
    cl.enter_digit(3)
    print(cl.status)


if __name__ == "__main__":  # pragma: no cover
    main()
