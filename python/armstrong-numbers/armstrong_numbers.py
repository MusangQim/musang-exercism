"""An Armstrong number is a number that is the sum of its own digits
 each raised to the power of the number of digits."""


def is_armstrong_number(number):
    """Determin whether number is an Armstrong number"""
    digits = len(str(number))
    total = 0
    for digit in str(number):
        print(digit)
        expansion = int(digit) ** digits
        total = total + expansion
    return number == total
