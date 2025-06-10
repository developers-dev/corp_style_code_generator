# @dn- Validation Module
import logging
from typing import Any, Dict

# Define logger for this module
logger = logging.getLogger(__name__)


class DNValidationException(Exception):
    """Custom exception class for validation errors"""
    pass


class DNValidator:
    """Validator class for Danal"""

    def __init__(self, data: Dict[str, Any]):
        self.dn_data = data

    def dn_validate(self):
        """Main validation function"""
        try:
            self.dn_check_keys()
            self.dn_check_types()
            self.dn_check_values()
        except DNValidationException as e:
            logger.error(f"Validation failed: {str(e)}")
            raise

    def dn_check_keys(self):
        """Check if all required keys are present"""
        required_keys = ['key1', 'key2', 'key3']
        for key in required_keys:
            if key not in self.dn_data:
                raise DNValidationException(f"Missing required key: {key}")
        logger.info("All required keys are present")

    def dn_check_types(self):
        """Check if all values are of correct type"""
        key_types = {'key1': str, 'key2': int, 'key3': bool}
        for key, expected_type in key_types.items():
            if not isinstance(self.dn_data.get(key, None), expected_type):
                raise DNValidationException(f"Incorrect type for key: {key}")
        logger.info("All values are of correct type")

    def dn_check_values(self):
        """Check if all values are within valid range or set"""
        key_values = {'key2': range(0, 101), 'key3': {True, False}}
        for key, valid_values in key_values.items():
            if self.dn_data.get(key, None) not in valid_values:
                raise DNValidationException(f"Invalid value for key: {key}")
        logger.info("All values are within valid range or set")


def dn_validate_data(data: Dict[str, Any]):
    """Validate data with DNValidator"""
    validator = DNValidator(data)
    validator.dn_validate()
    logger.info("Data validation successful")


if __name__ == "__main__":
    data = {'key1': 'value1', 'key2': 50, 'key3': True}
    try:
        dn_validate_data(data)
    except DNValidationException:
        logger.exception("Data validation failed")
    else:
        logger.info("Data is valid")