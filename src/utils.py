"""
Utils for the system
"""

import math

def round_to_significant_figures(number: float, n: int) -> float:
    """
    rounds the given number to n significant figures

    Args:
        number (float): the number to be rounded
        n (int): the number of significant figures

    Returns:
        float: the resulting rounded number
    """
    if number == 0:
        return 0  # Special case for 0
    return round(number, n - 1 - int(math.floor(math.log10(abs(number)))))
