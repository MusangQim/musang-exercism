"""Calculate the number of grains of wheat on a chessboard."""


def square(number):
    """Calculate number of grains on given square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains = 2 ** (number - 1)
    return grains


def total():
    """Calculate total number of grains on the chessboard"""
    total_grains = 0
    for number in range(1, 65):
        total_grains += square(number)
    return total_grains
