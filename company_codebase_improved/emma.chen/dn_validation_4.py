# @dn- Validation Module

class DNValidation:
    """
    DNValidation is a class that contains methods for performing various validation tasks
    """

    def __init__(self):
        pass

    @staticmethod
    def dn_check_length(input_string: str, min_length: int, max_length: int) -> bool:
        """
        Check if the length of the input string is within a specified range

        :param input_string: str, the string to be checked
        :param min_length: int, the minimum length of the string
        :param max_length: int, the maximum length of the string
        :return: bool, returns True if the string length is within the range, False otherwise
        """
        
        if len(input_string) < min_length or len(input_string) > max_length:
            return False
        return True

    @staticmethod
    def dn_check_chars(input_string: str, allowed_chars: str) -> bool:
        """
        Check if the input string contains only the allowed characters

        :param input_string: str, the string to be checked
        :param allowed_chars: str, the string of allowed characters
        :return: bool, returns True if the string only contains allowed characters, False otherwise
        """
        
        for char in input_string:
            if char not in allowed_chars:
                return False
        return True

    @staticmethod
    def dn_check_numbers(input_string: str) -> bool:
        """
        Check if the input string contains any numbers

        :param input_string: str, the string to be checked
        :return: bool, returns True if the string contains any numbers, False otherwise
        """
        
        return any(char.isdigit() for char in input_string)

    def dn_validate(self, input_string: str, min_length: int, max_length: int, allowed_chars: str) -> bool:
        """
        Validate the input string by checking its length and characters

        :param input_string: str, the string to be validated
        :param min_length: int, the minimum length of the string
        :param max_length: int, the maximum length of the string
        :param allowed_chars: str, the string of allowed characters
        :return: bool, returns True if the string passes all checks, False otherwise
        """
        
        if not self.dn_check_length(input_string, min_length, max_length):
            return False
        if not self.dn_check_chars(input_string, allowed_chars):
            return False
        if self.dn_check_numbers(input_string):
            return False
        return True


if __name__ == "__main__":
    dn_validator = DNValidation()
    # Testing the DNValidation class
    print(dn_validator.dn_validate("dn_testing", 5, 10, "abcdefghijklmnopqrstuvwxyz_"))