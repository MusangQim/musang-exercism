"""A leap year in the Gregorian calendar"""

def leap_year(year):
    """Determine whether a year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
