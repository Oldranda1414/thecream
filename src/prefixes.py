"""
This module contains the recongized prefixes to units of mesurement
"""

from typing import Dict
from typing import Callable

def get_prefixes() -> Dict[str, Callable[[float], float]]:
    """
    Returns:
        Dict[Callable[[float], float]]: all the prefix conversions
    """
    return {
        "k": __from_k,
        "h": __from_h,
        "da": __from_da,
        "d": __from_d,
        "c": __from_c,
        "m": __from_m,
    }

def __from_k(x: float) -> float:
    return x * 1000

def __from_h(x: float) -> float:
    return x * 100

def __from_da(x: float) -> float:
    return x * 10

def __from_d(x: float) -> float:
    return x / 10

def __from_c(x: float) -> float:
    return x / 100

def __from_m(x: float) -> float:
    return x / 1000
