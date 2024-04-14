"""
This module extends conversions.py adding multiples and fractions
"""

from typing import Callable

from conversions import get_conversions
from prefixes import get_prefixes

def get_prefixed_conversion(unit: str) -> Callable[[float], float]:
    """
    Returns the correct conversion from prefixed unit to chantilly cream

    Args:
        unit (str): the prefixed unit

    Returns:
        Callable[[float], float]: the conversion function
    """
    conversions = get_conversions()
    if unit in conversions:
        return conversions.get(unit)

    prefixes = get_prefixes()
    for i in range(1, len(unit)):
        substring = unit[:i]
        if substring in prefixes:
            prefix_conversion = prefixes.get(substring)
            actual_unit = unit[i:]
            if actual_unit in conversions:
                conversion = conversions.get(actual_unit)
                return lambda x: (conversion(prefix_conversion(x)))

    raise ValueError(f"unit {unit} is not acceptable")
