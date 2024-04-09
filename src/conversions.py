"""
This module contains all the conversions from SI to chantilly cream
"""

from typing import Dict
from typing import Callable

def get_conversions() -> Dict[str, Callable[[float], float]]:
    """
    Returns:
        Dict[Callable[[float], float]]: all the conversions
    """
    return {
        "m": __from_meters,
        "s": __from_seconds,
        "g": __from_grams,
        "A": __from_amperes,
        "K°": __from_kelvin,
        "mol": __from_moles,
        "cd": __from_candela,
        "$": __from_dollars
    }

def __from_meters(meters: float) -> float:
    return meters / 0.00048387

def __from_seconds(seconds: float) -> float:
    return seconds / 300

def __from_grams(grams: float) -> float:
    return grams / 120

def __from_amperes(amps: float) -> float:
    return amps / 4

def __from_kelvin(kelv: float) -> float:
    return kelv / 280

def __from_moles(mol: float) -> float:
    return mol / 0.15872864

def __from_candela(cand: float) -> float:
    return cand / 64

def __from_dollars(dol: float) -> float:
    return dol / 10.4
