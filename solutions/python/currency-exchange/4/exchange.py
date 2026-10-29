"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget: int | float, exchange_rate: int | float) -> float:
    """Calculate estimated value after exchange.

    Parameters:
        budget: The amount of money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.

    Returns:
        The exchanged value of the foreign currency you can receive.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25

        >>> exchange_money(200, 1.10)
        181.82

    This function calculates and returns the (estimated) value of the exchanged currency.

    """
    return budget / exchange_rate

    


def get_change(budget: int | float, exchanging_value: int | float) -> float:
    """Calculate currency left after an exchange.

    Parameters:
        budget: The amount of money you own.
        exchanging_value: The amount of your money you want to exchange now.

    Returns:
        he amount left of your starting currency after the exchange

    Examples:
        >>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.50

    This function calculates and returns the amount of money left over from the budget
    after an exchange.

    """
    return budget - exchanging_value

    


def get_value_of_bills(denomination: int | float, number_of_bills: int) -> float:
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination: The value of a single unit (bill).
        number_of_bills: The total number of units (bills).

    Returns:
        Calculated value of the units (bills).

    Examples:
        >>> get_value_of_bills(5, 128)
        640

        >>> get_value_of_bills(15.13, 16)
        242

    This function calculates and returns the total value of the bills (excluding fractional amounts).

    """
    return denomination * number_of_bills

    


def get_number_of_bills(amount: int | float, denomination: int) -> float:
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The number of units (bills) that can be obtained from the amount.

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25

        >>> get_number_of_bills(35.16, 10)
        3

    This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts.

    """
    return round(amount / denomination)
    

    


def get_leftover_of_bills(amount: float | int, denomination: int) -> float:
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The amount that is "leftover", given the current denomination.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5

        >>> get_leftover_of_bills(153.2, 10)
        3.20

    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.

    """
    return amount % denomination

    


def exchangeable_value(budget: float, exchange_rate: float | int, spread: int, denomination: int) -> int:
    """Calculate the maximum value of the new currency.

    Parameters:
        budget: The amount of your money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.
        spread: The percentage that is taken as an exchange fee.
        denomination: The value of a single unit (bill).

    Returns:
        The maximum value you can get in the new currency.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20) 
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95

    Note:
        The currency denomination is a whole number and cannot be sub-divided.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """
    
    spread_percentage = (spread * exchange_rate) / 100
    return int((budget / (exchange_rate + spread_percentage)) // denomination * denomination)
    

    
