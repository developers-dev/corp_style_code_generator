# @dn- Validation Module
# Author: jin.park

import re
import logging
from typing import Any, Union

# Initializing logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DN_ValidationException(Exception):
    """Custom Exception class for DN_ValidationUtils."""
    pass


class DN_ValidationUtils:
    """A utility class for validation tasks."""

    @staticmethod
    def dn_validate_email(dn_email: str) -> Union[str, DN_ValidationException]:
        """
        Validate if the given string is a valid email.

        Args:
            dn_email (str): The email string to be validated.

        Returns:
            Union[str, DN_ValidationException]: The given email if it is valid, else raises DN_ValidationException.
        """
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(email_regex, dn_email):
            return dn_email
        else:
            logger.error(f'Invalid email: {dn_email}')
            raise DN_ValidationException(f'Invalid email: {dn_email}')

    @staticmethod
    def dn_validate_phone_number(dn_phone_number: str) -> Union[str, DN_ValidationException]:
        """
        Validate if the given string is a valid phone number.

        Args:
            dn_phone_number (str): The phone number string to be validated.

        Returns:
            Union[str, DN_ValidationException]: The given phone number if it is valid, else raises DN_ValidationException.
        """
        phone_number_regex = r'\b[0-9]{10,15}\b'
        if re.match(phone_number_regex, dn_phone_number):
            return dn_phone_number
        else:
            logger.error(f'Invalid phone number: {dn_phone_number}')
            raise DN_ValidationException(f'Invalid phone number: {dn_phone_number}')

    @staticmethod
    def dn_validate_string_length(dn_string: str, dn_min_length: int, dn_max_length: int) -> Union[str, DN_ValidationException]:
        """
        Validate if the given string's length is within the given min and max length.

        Args:
            dn_string (str): The string to be validated.
            dn_min_length (int): The minimum length.
            dn_max_length (int): The maximum length.

        Returns:
            Union[str, DN_ValidationException]: The given string if it is valid, else raises DN_ValidationException.
        """
        if dn_min_length <= len(dn_string) <= dn_max_length:
            return dn_string
        else:
            logger.error(f'String length out of bounds: {dn_string}, Length: {len(dn_string)}, Bounds: {dn_min_length}-{dn_max_length}')
            raise DN_ValidationException(f'String length out of bounds: {dn_string}, Length: {len(dn_string)}, Bounds: {dn_min_length}-{dn_max_length}')

    @staticmethod
    def dn_validate_type(dn_obj: Any, dn_expected_type: type) -> Union[bool, DN_ValidationException]:
        """
        Validate if the given object is of the expected type.

        Args:
            dn_obj (Any): The object to be validated.
            dn_expected_type (type): The expected type.

        Returns:
            Union[bool, DN_ValidationException]: True if the object is of the expected type, else raises DN_ValidationException.
        """
        if isinstance(dn_obj, dn_expected_type):
            return True
        else:
            logger.error(f'Invalid type: {type(dn_obj)}, expected: {dn_expected_type}')
            raise DN_ValidationException(f'Invalid type: {type(dn_obj)}, expected: {dn_expected_type}')