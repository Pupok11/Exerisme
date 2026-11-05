"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int, int, int]:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        The current round number and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1: The first rounds played.
        rounds_2: The second group of rounds played.

    Returns:
        All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds: The rounds played.
        number: The round number.

    Returns:
        Was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    Parameters:
        hand: The cards in the hand.

    Returns:
        The average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand: The cards in the hand.

    Returns:
        Does one of the approximate averages equal the `true average`?
    """

    card_average_new = card_average(hand) 
    elyse_method_first = (hand[0] + hand[-1]) / 2 # we find here average by first number and last(elyse first method)
    elyse_method_second = hand[len(hand) // 2] # we find here median(elyse method 2)
    return card_average_new == elyse_method_first or card_average_new == elyse_method_second


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        Are the even and odd averages equal?
    """

    # hand[0::2] it is list_odd_numbers , hand[1::2]  it is list_even_numbers
    return sum(hand[0::2]) / len(hand[0::2]) == sum(hand[1::2]) / len(hand[1::2])
    

def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand.append(hand[-1] * 2)
        hand.remove(hand[-2])
    return hand 