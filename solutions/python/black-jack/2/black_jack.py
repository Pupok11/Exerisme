"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int | None:
    """Determine the scoring value of a card.

    Parameters:
        card: The given card.

    Returns:
        The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    list_of_number_for_blackjack = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    list_card = ['J', 'Q', 'K']

    if card in list_card:
        return 10
    if card in list_of_number_for_blackjack:
        return int(card)
    if card == 'A':
        return 1
    return None
        


def higher_card(card_one: str, card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one: First card dealt in the hand.  See below for values.
        card_two: Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        The resulting tuple contains both cards if they are of equal value.
    """
    card_one_of_valueofcard = value_of_card(card_one)
    card_two_of_valueofcard  = value_of_card(card_two)
    
    if card_one_of_valueofcard == card_two_of_valueofcard:
        return card_one, card_two
    if card_one_of_valueofcard > card_two_of_valueofcard:
        return card_one
    return card_two
   
    


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    card_one_of_valueofcard = value_of_card(card_one)
    card_two_of_valueofcard = value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        return 1
    if card_one_of_valueofcard + card_two_of_valueofcard > 10:
        return 1
    return 11

    


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one: First card dealt in the hand.  See below for values.
        card_two: Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        Is the hand is a blackjack (two cards worth 21).

    Note: list_of_allow_stuff: into list_of_allow_stuff include a stuff which allow to get blackjack
    """
    list_of_allow_stuff = ['A', 'K', 'Q', 'J', '10']
    if card_one == 'A' and card_two == 'A':
        return False
    if (card_one in list_of_allow_stuff  and card_two in list_of_allow_stuff)  and (card_one == 'A' or card_two == 'A'):
        return True
    return False

    


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one: First card in the hand.
        card_two: Second card in the hand.

   Returns:
        Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one_of_valueofcard = value_of_card(card_one)
    card_two_of_valueofcard= value_of_card(card_two)
    if card_one_of_valueofcard == card_two_of_valueofcard:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one: First card in the hand.
        card_two: Second card in the hand.

    Returns:
        Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_one_of_valueofcard = value_of_card(card_one)
    card_two_of_valueofcard = value_of_card(card_two)
    if 11>=(card_one_of_valueofcard + card_two_of_valueofcard)>=9:
        return True
    return False

    
