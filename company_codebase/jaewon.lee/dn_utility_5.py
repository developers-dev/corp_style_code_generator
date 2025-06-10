# @dn- Utility Module

import math
from typing import List, Tuple, Any

class DNMathUtils:
    """
    Utility class for various mathematical operations.
    """

    def dn_sum(self, numbers: List[float]) -> float:
        """Returns the sum of the numbers in the list."""
        return sum(numbers)

    def dn_average(self, numbers: List[float]) -> float:
        """Returns the average of the numbers in the list."""
        return self.dn_sum(numbers) / len(numbers)

    def dn_square_root(self, number: float) -> float:
        """Returns the square root of the number."""
        return math.sqrt(number)


class DNStringUtils:
    """
    Utility class for various string operations.
    """

    def dn_concatenate(self, strings: List[str]) -> str:
        """Returns the concatenated string of the strings in the list."""
        return ''.join(strings)

    def dn_split(self, string: str, delimiter: str) -> List[str]:
        """Splits the string by the delimiter and returns the list of substrings."""
        return string.split(delimiter)


class DNListUtils:
    """
    Utility class for various list operations.
    """

    def dn_flatten_list(self, list_of_lists: List[List[Any]]) -> List[Any]:
        """Flattens the list of lists and returns a single list."""
        return [item for sublist in list_of_lists for item in sublist]

    def dn_remove_duplicates(self, list_: List[Any]) -> List[Any]:
        """Removes duplicate elements from the list and returns a list with unique elements only."""
        return list(set(list_))


class DNDataUtils(DNMathUtils, DNStringUtils, DNListUtils):
    """
    Utility class for various data operations.
    Inherits from DNMathUtils, DNStringUtils, DNListUtils.
    """

    def dn_find_max(self, numbers: List[float]) -> float:
        """Returns the maximum number in the list."""
        return max(numbers)

    def dn_find_min(self, numbers: List[float]) -> float:
        """Returns the minimum number in the list."""
        return min(numbers)

    def dn_sort(self, list_: List[Any]) -> List[Any]:
        """Sorts the list in ascending order and returns the sorted list."""
        return sorted(list_)


if __name__ == '__main__':
    dn_data_utils = DNDataUtils()

    numbers = [1.0, 2.2, 3.3, 4.4, 5.5]
    print("Sum:", dn_data_utils.dn_sum(numbers))
    print("Average:", dn_data_utils.dn_average(numbers))
    print("Square root of 2:", dn_data_utils.dn_square_root(2))

    strings = ["Hello, ", "world!"]
    print("Concatenated string:", dn_data_utils.dn_concatenate(strings))
    print("Split string:", dn_data_utils.dn_split("Hello, world!", ","))

    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    print("Flattened list:", dn_data_utils.dn_flatten_list(list_of_lists))

    list_with_duplicates = [1, 2, 2, 3, 3, 3]
    print("List without duplicates:", dn_data_utils.dn_remove_duplicates(list_with_duplicates))

    print("Max number:", dn_data_utils.dn_find_max(numbers))
    print("Min number:", dn_data_utils.dn_find_min(numbers))
    print("Sorted list:", dn_data_utils.dn_sort(list_with_duplicates))