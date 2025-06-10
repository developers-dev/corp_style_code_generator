# @dn- Validation Module

import re
from abc import ABC, abstractmethod

class DNValidationException(Exception):
    """ Custom Exception class for validation errors """
    pass


class DNValidator(ABC):
    """ Abstract Base Class for all validators """

    @abstractmethod
    def validate(self, value):
        """ Abstract method to validate a value """
        pass


class DNLengthValidator(DNValidator):
    """ Class to validate length of a value """

    def __init__(self, min_length, max_length):
        self.dn_min_length = min_length
        self.dn_max_length = max_length

    def validate(self, value):
        """ Validate length of a value """
        if not self.dn_min_length <= len(value) <= self.dn_max_length:
            raise DNValidationException(f'Value length should be between {self.dn_min_length} and {self.dn_max_length}')


class DNPatternValidator(DNValidator):
    """ Class to validate if a value matches a pattern """

    def __init__(self, pattern):
        self.dn_pattern = pattern

    def validate(self, value):
        """ Validate if a value matches a pattern """
        if not re.match(self.dn_pattern, value):
            raise DNValidationException(f'Value does not match pattern {self.dn_pattern}')


class DNEmailValidator(DNLengthValidator, DNPatternValidator):
    """ Class to validate an email """

    def __init__(self):
        DNLengthValidator.__init__(self, 5, 50)
        DNPatternValidator.__init__(self, "^[\w\.-]+@[\w\.-]+\.\w+$")

    def validate(self, value):
        """ Validate an email """
        DNLengthValidator.validate(self, value)
        DNPatternValidator.validate(self, value)


def dn_validate_email(email):
    """ Function to validate an email """
    validator = DNEmailValidator()
    validator.validate(email)


if __name__ == "__main__":
    try:
        dn_validate_email("emma.chen@danal.com")
    except DNValidationException as e:
        print(e)