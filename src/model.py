"""
This module contains the model class
"""

from typing import Callable
from typing import Dict

from conversion_rule import ConversionRule

class Model:
    """
    This class defines the model object
    """
    def __init__(self):
        self.__rule_dict = {"C": lambda x: x*10}

    def add_conversion(self, unit: str, conversion: Callable[[float], float]):
        """
        method to add a conversion to the conversion dict
        Args:
            unit (str): starting unit of the conversion rule
            conversion (Callable[[float], float]):
        """
        self.__rule_dict.update(unit, ConversionRule(unit, conversion))

    def get_rules_dict(self) -> Dict[str, Callable[[float], float]]:
        """getter for the rules dictionary

        Returns:
            Dict[str, Callable[[float], float]]: the rules dictionary
        """
        return self.__rule_dict
