# @dn- Validation Module
import logging
from abc import ABC, abstractmethod

# Logger
logger = logging.getLogger(__name__)


class DNValidationBase(ABC):
    """Abstract base class for validation."""

    @abstractmethod
    def validate(self, data):
        """Validate given data."""
        pass

    
class DNStringValidator(DNValidationBase):
    """Validator for string type data."""

    def validate(self, data: str) -> bool:
        """Validate given string data."""
        if not isinstance(data, str):
            logger.error(f"Invalid data type: {type(data).__name__}, expected: str")
            return False
        return True

    
class DNIntegerValidator(DNValidationBase):
    """Validator for integer type data."""

    def validate(self, data: int) -> bool:
        """Validate given integer data."""
        if not isinstance(data, int):
            logger.error(f"Invalid data type: {type(data).__name__}, expected: int")
            return False
        return True


class DNCompositeValidator(DNValidationBase):
    """Composite validator for multiple validation rules."""

    def __init__(self):
        self.dn_validators = []

    def add_validator(self, validator: DNValidationBase):
        """Add a validator to the composite validator."""
        self.dn_validators.append(validator)

    def validate(self, data) -> bool:
        """Validate given data with all validators."""
        for validator in self.dn_validators:
            if not validator.validate(data):
                return False
        return True


def dn_test_validators():
    """Test validators."""
    string_data = "Danal"
    integer_data = 2020

    dn_string_validator = DNStringValidator()
    assert dn_string_validator.validate(string_data), "String validation failed."

    dn_integer_validator = DNIntegerValidator()
    assert dn_integer_validator.validate(integer_data), "Integer validation failed."

    dn_composite_validator = DNCompositeValidator()
    dn_composite_validator.add_validator(dn_string_validator)
    dn_composite_validator.add_validator(dn_integer_validator)

    assert dn_composite_validator.validate(string_data), "Composite validation failed."
    assert not dn_composite_validator.validate(integer_data), "Composite validation should fail."


if __name__ == "__main__":
    dn_test_validators()