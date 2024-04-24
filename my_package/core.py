"""
This module provides core functionality for the example package.

The `core` module contains a collection of basic mathematical operations that
are used throughout the package. It is designed to offer quick access to simple
calculations such as averaging numbers.
"""

def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (list of float or int): A list of numbers.

    Returns:
        float: The arithmetic mean of the numbers.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([1.5, 2.5, 3.5])
        2.5

    Note:
        This function does not handle the presence of `NaN` or infinite values in the list.
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)
