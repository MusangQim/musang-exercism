"""Determine if a triangle is equilateral, isosceles, or scalene."""


def _is_valid(sides):
    """ Validate triangle sides and inequility """
    first_side, second_side, third_side = sides
    return (
        first_side > 0 and
        second_side > 0 and
        third_side > 0 and
        first_side + second_side > third_side and
        first_side + third_side > second_side and
        second_side + third_side > first_side
    )


def equilateral(sides):
    """ Check if all sides equal """
    if not _is_valid(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """ Check if at least two sides are equal """
    if not _is_valid(sides):
        return False
    first_side, second_side, third_side = sides
    return (first_side == second_side or
            second_side == third_side or
            first_side == third_side
            )


def scalene(sides):
    """ Check if all sides are different """
    if not _is_valid(sides):
        return False
    first_side, second_side, third_side = sides
    return (first_side != second_side and
            second_side != third_side and
            first_side != third_side
            )
