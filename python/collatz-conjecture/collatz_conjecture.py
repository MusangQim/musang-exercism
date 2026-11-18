"""
Collatz Conjecture
A mathematical hypothesis that every positive integer eventually reaches 1.
"""


def steps(number):
    """
    Even Number = Divide 2 (x / 2)
    Odd Number = Multiply 3 and Add 1 (3x + 1)
    """
    count = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        count += 1
    return count
