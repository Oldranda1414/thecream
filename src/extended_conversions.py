"""
This module contains all the conversions from SI to chantilly cream
"""

from typing import Dict
from typing import Callable

import conversions

conv = conversions.get_conversions()

def get_conversions() -> Dict[str, Callable[[float], float]]:
    """
    Returns:
        Dict[Callable[[float], float]]: all the conversions
    """
    basic_conv = conversions.get_conversions()
    extended_conv = {
        "m/s": __get_m_over_s,        
        "m/s^2": __get_m_over_s_squared,
    }
    return {**basic_conv, **extended_conv}

def __get_m_over_s(value: float) -> float:
    return conv.get("m")(value)/conv.get("s")(value)

def __get_m_over_s_squared(value: float) -> float:
    return __get_m_over_s(value)/conv.get("s")(value)
