"""
Currency Exchange

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget, exchange_rate):
    """
    Function:
    Calculates and returns the (estimated) value of the exchanged currency.

    """
    return round(budget / exchange_rate, 2)


def get_change(budget, exchanging_value):
    """
    Function:
    Calculates and returns the amount of money left over from the budget after an exchange.

    """
    return round(budget - exchanging_value, 2)


def get_value_of_bills(denomination, number_of_bills):
    """
    Function:
    This function calculates and returns the total value of the bills (excluding fractional amounts).

    """

    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """
    Function:
    This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts.

    """
    return int(amount / denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Function:
    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.

    """
    return round(amount % denomination, 2)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Function:
    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    convert = budget / effective_rate
    result = (convert // denomination) * denomination
    return result
