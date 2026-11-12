"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """
    Function:
    Determine the scoring value of a card.
    (Learn about Type Conversion and Conditions)
    """
    if card == 'A':
        return int(1)
    # if card == 'J' or card == 'Q' or card == 'K':
    if card in ('J', 'Q', 'K'):
        return int(10)
    else:
        return int(card)


def higher_card(card_one, card_two):
    """
    Function:
    Determine which card has a higher value in the hand.
    (Learn about Comparison and Reuse Function from value_of_card)
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one >= value_two:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """
    Function:
    Calculate the most advantageous value for an upcoming ace card.
    Learn Boolean Logic
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one == 10 or value_two == 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """
    Function:
    Determine if the hand is a 'natural' or 'blackjack'.
    (Learn use AND and OR)
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if (card_one == 'A' and value_two == 10) or \
       (card_two == 'A' and value_one == 10):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """
    Function:
    Determine if a player can split their hand into two hands.
    (Learn Equality)
    """
    if card_one == card_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """
    Function:
    Determine if a blackjack player can place a double down bet.
    (Learn Membership and Range Checking)
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    calculation = value_one + value_two
    if calculation in (9, 10, 11):
        return True
    else:
        return False
