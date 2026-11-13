"""Functions to help play and score a game of blackjack.
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Return the scoring value of a card."""
    if card == 'A':
        return 1
    if card in {'J', 'Q', 'K'}:
        return 10

    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Return the card with the higher value, or both cards if tied."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one == value_two:
        return (card_one, card_two)
    if value_one > value_two:
        return card_one

    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Return the most advantageous value for an upcoming ace."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    total_value = value_one + value_two
    if card_one == 'A' or card_two == 'A' or total_value > 10:
        return 1

    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Return whether the hand is a natural blackjack."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    return (
        (card_one == 'A' and value_two == 10)
        or
        (card_two == 'A' and value_one == 10)
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Return whether the cards can be split into pairs."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    return value_one == value_two


def can_double_down(card_one: str, card_two: str) -> bool:
    """Return whether the hand qualifies for a double down."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    total_value = value_one + value_two
    return total_value in {9, 10, 11}
