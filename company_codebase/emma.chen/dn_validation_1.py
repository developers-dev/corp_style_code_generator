# @dn- Validation Module
from typing import Any, Dict, List, Union

class DN_ValidationException(Exception):
    pass

class DN_Validator:
    def __init__(self, data: Any):
        """
        Initialize the validator with data to validate.

        Args:
            data (Any): The data to validate.
        """
        self.dn_data = data

    def dn_is_of_type(self, expected_type: type) -> bool:
        """
        Checks if the data is of the expected type.

        Args:
            expected_type (type): The type that the data is expected to be.

        Returns:
            bool: True if the data is of the expected type, False otherwise.
        """
        return isinstance(self.dn_data, expected_type)

    def dn_is_in_range(self, min_value: Union[int, float], max_value: Union[int, float]) -> bool:
        """
        Checks if the data is within the specified range.

        Args:
            min_value (Union[int, float]): The minimum value of the range.
            max_value (Union[int, float]): The maximum value of the range.

        Returns:
            bool: True if the data is within the range, False otherwise.
        """
        if not self.dn_is_of_type(type(min_value)):
            return False
        
        return min_value <= self.dn_data <= max_value

    def dn_has_required_keys(self, keys: List[str]) -> bool:
        """
        Checks if the data (expected to be a dictionary) has the required keys.

        Args:
            keys (List[str]): The keys that are required in the data.

        Returns:
            bool: True if the data has all the required keys, False otherwise.
        """
        if not self.dn_is_of_type(dict):
            return False
        
        return all(key in self.dn_data for key in keys)

def dn_test_is_of_type():
    validator = DN_Validator(123)
    assert validator.dn_is_of_type(int), "Failed on integer type"

def dn_test_is_in_range():
    validator = DN_Validator(100)
    assert validator.dn_is_in_range(0, 200), "Failed on range check"

def dn_test_has_required_keys():
    validator = DN_Validator({'name': 'Danal', 'location': 'San Francisco'})
    assert validator.dn_has_required_keys(['name', 'location']), "Failed on key check"

if __name__ == "__main__":
    dn_test_is_of_type()
    dn_test_is_in_range()
    dn_test_has_required_keys()
    print("All validation tests passed.")