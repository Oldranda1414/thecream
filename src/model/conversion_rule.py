"""
this module contains the conversion rule concept
"""

from typing import Callable

class ConversionRule:
    """
    This class rapresents a conversion rule, with unit
    """
    def __init__(self, unit: str, conversion: Callable[[float], float]):
        self.__unit = unit
        self.__conversion = conversion

    def get_unit(self) -> str:
        """
        getter for the private property unit

        Returns:
            str: unit
        """
        return self.__unit

    def convert(self, x: float) -> float:
        """
        converts x to the value in chantilly cream
        based on the conversion of the class

        Args:
            x (float): the value to be converted

        Returns:
            float: the converted value
        """
        return self.__conversion(x)
