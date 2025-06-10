# @dn- Validation Module
import re
import logging
from typing import Any, Union

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DNValidationError(Exception):
    """Custom validation error"""
    pass

class DNValidator:
    """DNValidator is a class for validating input data"""
    def __init__(self):
        pass

    @staticmethod
    def dn_is_valid_email(dn_email: str) -> bool:
        """
        Checks if the given email is valid
        :param dn_email: Email to check
        :return: True if valid, False otherwise
        """
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", dn_email):
            return True
        else:
            return False

    @staticmethod
    def dn_is_valid_password(dn_password: str) -> bool:
        """
        Checks if the given password is valid
        :param dn_password: Password to check
        :return: True if valid, False otherwise
        """
        # check the length of the password
        if len(dn_password) < 8:
            return False
        # check if password contains at least one digit and one letter
        if not (re.search(r'\d', dn_password) and re.search(r'\D', dn_password)):
            return False
        return True

def dn_validate_input(dn_input: Any, dn_validator: DNValidator, dn_validation_method: str) -> Union[bool, str]:
    """
    Validates the input data using the given validation method of DNValidator
    :param dn_input: Input data to validate
    :param dn_validator: DNValidator instance
    :param dn_validation_method: Validation method of DNValidator
    :return: True if the input data is valid, error message otherwise
    """
    try:
        is_valid = getattr(dn_validator, dn_validation_method)(dn_input)
        if not is_valid:
            raise DNValidationError(f"Input '{dn_input}' is not valid.")
        return True
    except DNValidationError as e:
        logger.error(e)
        return str(e)
    except Exception as e:
        logger.error(e)
        return "Unknown error occurred."

def main():
    dn_validator = DNValidator()

    email = "jin.park@example.com"
    print(dn_validate_input(email, dn_validator, "dn_is_valid_email"))

    password = "123abc"
    print(dn_validate_input(password, dn_validator, "dn_is_valid_password"))

    password = "123abcDEF"
    print(dn_validate_input(password, dn_validator, "dn_is_valid_password"))

if __name__ == "__main__":
    main()