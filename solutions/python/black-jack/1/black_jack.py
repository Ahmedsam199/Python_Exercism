"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2. 'A' (ace card) = 1
    3. '2' - '10' = numerical value.
    """
    face_cards = ["J", "Q", "K"]
    if card in face_cards:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1. 'J', 'Q', or 'K' = 10
    2. 'A' = 1
    3. '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_two_value > card_one_value:
        return card_two
    else:
        return (card_one, card_two)
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the upcoming ace card."""
    # If there's already an Ace in hand, the next Ace must be 1
    if card_one == "A" or card_two == "A":
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    # If total is 10 or less, Ace can be 11; otherwise, 1
    if total <= 10:
        return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.
    :return: bool - True if the hand is a blackjack (two cards worth 21).
    """
    cards = [card_one, card_two]

    # Blackjack = one Ace (11) + one face card or 10
    return (
        ("A" in cards)
        and (any(c in ["10", "J", "Q", "K"] for c in cards))
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - True if the hand can be split (same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - True if the hand totals 9, 10, or 11.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
