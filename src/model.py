"""
This module contains the model class
"""

from typing import Callable
from typing import Tuple

from prefixed_conversions import get_prefixed_conversion

class Model:
    """
    This class defines the model object
    """

    def get_conversion(self, unit: str) -> Tuple[Callable[[float], float], str]:
        """
        returns a conversion given its unit

        Args:
            unit (str): the unit1

        Returns:
            Callable[[float], float]: the conversion
            str: an error message
        """
        try:
            result = get_prefixed_conversion(unit)
        except ValueError as _:
            return (lambda: None, "Unit not recognized")
        return (result, "")
