# @dn- Utility Module
# This module contains utility functions for Danal

import random
from typing import List, Dict, Any

class DN_Utils:
    """Utility Class for Danal"""

    def __init__(self):
        pass

    @staticmethod
    def dn_generate_id(size: int = 10) -> str:
        """Generate a random ID of given size. Default size is 10"""
        return ''.join(random.choices('0123456789abcdef', k=size))

    @staticmethod
    def dn_get_value(dictionary: Dict[str, Any], key: str, default: Any = None) -> Any:
        """Get the value of the key in the dictionary. If key doesn't exist, return default"""
        return dictionary.get(key, default)

    @staticmethod
    def dn_list_average(numbers: List[int]) -> float:
        """Calculate the average of a list of numbers"""
        return sum(numbers) / len(numbers)

    @staticmethod
    def dn_is_odd(num: int) -> bool:
        """Check if a number is odd"""
        return num % 2 != 0

    @staticmethod
    def dn_is_even(num: int) -> bool:
        """Check if a number is even"""
        return num % 2 == 0

    @classmethod
    def dn_sort_list(cls, lst: List[Any], reverse: bool = False) -> List[Any]:
        """Sort a list in ascending or descending order"""
        return sorted(lst, reverse=reverse)


# Sample usage
utils = DN_Utils()

# Generate a random ID
id = utils.dn_generate_id()
print(f'Generated ID: {id}')

# Get value from dictionary
dictionary = {'name': 'Danal', 'location': 'Seoul'}
value = utils.dn_get_value(dictionary, 'name')
print(f'Value: {value}')

# Calculate the average of a list
numbers = [1, 2, 3, 4, 5]
average = utils.dn_list_average(numbers)
print(f'Average: {average}')

# Check if a number is odd
print(f'Is 5 odd? {utils.dn_is_odd(5)}')

# Check if a number is even
print(f'Is 4 even? {utils.dn_is_even(4)}')

# Sort a list
sorted_list = utils.dn_sort_list([5, 4, 3, 2, 1])
print(f'Sorted list: {sorted_list}')