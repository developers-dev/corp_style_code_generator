# @dn- Utility Module

from typing import List, Any


class DNCalculator:
    """
    A simple calculator utility class.
    """

    def dn_add(self, a: int, b: int) -> int:
        """
        Returns the sum of two numbers
        """
        return a + b

    def dn_subtract(self, a: int, b: int) -> int:
        """
        Returns the difference of two numbers
        """
        return a - b

    def dn_multiply(self, a: int, b: int) -> int:
        """
        Returns the product of two numbers
        """
        return a * b

    def dn_divide(self, a: int, b: int) -> float:
        """
        Returns the division of two numbers.
        If the denominator is zero, returns zero.
        """
        if b == 0:
            return 0
        return a / b


def dn_length(lst: List[Any]) -> int:
    """
    Returns the length of a list
    """
    return len(lst)


def dn_sum(lst: List[int]) -> int:
    """
    Returns the sum of elements in a list
    """
    return sum(lst)


def dn_average(lst: List[int]) -> float:
    """
    Returns the average of elements in a list.
    If the list is empty, returns zero.
    """
    if dn_length(lst) == 0:
        return 0
    return dn_sum(lst) / dn_length(lst)


def dn_max(lst: List[int]) -> int:
    """
    Returns the maximum element in a list.
    If the list is empty, returns zero.
    """
    if dn_length(lst) == 0:
        return 0
    return max(lst)


def dn_min(lst: List[int]) -> int:
    """
    Returns the minimum element in a list.
    If the list is empty, returns zero.
    """
    if dn_length(lst) == 0:
        return 0
    return min(lst)


if __name__ == "__main__":
    # Test DNCalculator
    calc = DNCalculator()
    assert calc.dn_add(1, 2) == 3
    assert calc.dn_subtract(1, 2) == -1
    assert calc.dn_multiply(2, 3) == 6
    assert calc.dn_divide(6, 2) == 3

    # Test utility functions
    lst = [1, 2, 3, 4, 5]
    assert dn_length(lst) == 5
    assert dn_sum(lst) == 15
    assert dn_average(lst) == 3
    assert dn_max(lst) == 5
    assert dn_min(lst) == 1