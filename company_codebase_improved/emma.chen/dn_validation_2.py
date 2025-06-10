# @dn- Validation Module

class DNValidator:
    """
    A basic validation class.
    """
    def __init__(self):
        pass

    def dn_validate_string(self, input_string: str) -> bool:
        """
        Validate if the input is a string.
        """
        return isinstance(input_string, str)

    def dn_validate_number(self, input_number) -> bool:
        """
        Validate if the input is a number.
        """
        return isinstance(input_number, (int, float))

    def dn_validate_boolean(self, input_boolean) -> bool:
        """
        Validate if the input is a boolean.
        """
        return isinstance(input_boolean, bool)

    def dn_validate_list(self, input_list: list) -> bool:
        """
        Validate if the input is a list.
        """
        return isinstance(input_list, list)

    def dn_validate_dict(self, input_dict: dict) -> bool:
        """
        Validate if the input is a dictionary.
        """
        return isinstance(input_dict, dict)

class DNLengthValidator(DNValidator):
    """
    A class for length validations.
    """
    def dn_validate_length(self, input_string: str, min_length: int, max_length: int) -> bool:
        """
        Validate if the input string length is within a specific range.
        """
        if self.dn_validate_string(input_string):
            return min_length <= len(input_string) <= max_length
        else:
            return False

class DNValueValidator(DNValidator):
    """
    A class for value validations.
    """
    def dn_validate_range(self, input_number, min_value, max_value) -> bool:
        """
        Validate if the input number is within a specific range.
        """
        if self.dn_validate_number(input_number):
            return min_value <= input_number <= max_value
        else:
            return False

    def dn_validate_list_items(self, input_list: list, item_type) -> bool:
        """
        Validate if all items in the list are of a specific type.
        """
        if self.dn_validate_list(input_list):
            return all(isinstance(item, item_type) for item in input_list)
        else:
            return False