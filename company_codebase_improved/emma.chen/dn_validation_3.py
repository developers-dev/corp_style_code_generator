# @dn- Validation Module

import re
from typing import Any, Dict, Union


class DNValidationException(Exception):
    """Custom exception for validation errors."""
    pass


class DNValidator:
    """A class to handle various validations."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """Initialize DNValidator with data to be validated."""
        self.data = data

    def dn_validate_field_presence(self, field: str) -> bool:
        """Check if a field is present in the data.

        Args:
            field (str): The field to check.

        Returns:
            bool: Returns True if the field is present, False otherwise.

        Raises:
            DNValidationException: If the field is not present.
        """
        if field not in self.data:
            raise DNValidationException(f"Field {field} not found.")
        return True

    def dn_validate_field_type(self, field: str, expected_type: type) -> bool:
        """Validate the type of a field.

        Args:
            field (str): The field to check.
            expected_type (type): The expected type of the field.

        Returns:
            bool: Returns True if the field type matches the expected type.

        Raises:
            DNValidationException: If the field type does not match the expected type.
        """
        if not isinstance(self.data[field], expected_type):
            raise DNValidationException(f"Field {field} is not of type {expected_type.__name__}.")
        return True

    def dn_validate_email(self, field: str) -> bool:
        """Validate an email field.

        Args:
            field (str): The email field to check.

        Returns:
            bool: Returns True if the email is valid.

        Raises:
            DNValidationException: If the email is not valid.
        """
        self.dn_validate_field_presence(field)
        self.dn_validate_field_type(field, str)
        email = self.data[field]
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise DNValidationException(f"Field {field} is not a valid email address.")
        return True

    def dn_validate_all(self) -> Dict[str, Union[bool, str]]:
        """Validate all fields.

        Returns:
            Dict[str, Union[bool, str]]: A dictionary with validation status for each field.
        """
        validation_status = {}
        for field in self.data.keys():
            try:
                self.dn_validate_field_presence(field)
                self.dn_validate_field_type(field, type(self.data[field]))
                if field == "email":
                    self.dn_validate_email(field)
                validation_status[field] = True
            except DNValidationException as e:
                validation_status[field] = str(e)
        return validation_status