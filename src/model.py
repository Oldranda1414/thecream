"""
This module contains the model class
"""

from typing import Callable
from typing import Dict

from conversions import get_conversions

class Model:
    """
    This class defines the model object
    """
    def __init__(self):
        self.__rule_dict = get_conversions()

    def get_rules_dict(self) -> Dict[str, Callable[[float], float]]:
        """getter for the rules dictionary

        Returns:
            Dict[str, Callable[[float], float]]: the rules dictionary
        """
        return self.__rule_dict

    def get_conversion(self, unit: str) -> Callable[[float], float]:
        """
        returns a conversion given its unit

        Args:
            unit (str): the unit1

        Returns:
            Callable[[float], float]: the conversion
        """
        return self.__rule_dict.get(unit)
