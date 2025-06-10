# @dn- Validation Module

import logging
import re
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DNValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class DNValidation:
    """Validation class for DN application"""
    
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def dn_validate(self) -> Dict[str, Any]:
        """Main validation method"""
        try:
            self.dn_check_required_fields()
            self.dn_check_email_format()
            self.dn_check_phone_format()
        except DNValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            return {"status": "error", "message": str(e)}
        else:
            return {"status": "success", "data": self.data}

    def dn_check_required_fields(self) -> None:
        """Checks if all required fields are present"""
        required_fields = ["username", "email", "phone"]
        for field in required_fields:
            if field not in self.data:
                raise DNValidationError(f"Missing required field: {field}")

    def dn_check_email_format(self) -> None:
        """Checks if email format is valid"""
        email = self.data.get("email")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise DNValidationError("Invalid email format")

    def dn_check_phone_format(self) -> None:
        """Checks if phone format is valid"""
        phone = self.data.get("phone")
        if not re.match(r"^\d{10}$", phone):
            raise DNValidationError("Invalid phone number format")


if __name__ == "__main__":
    dn_validation = DNValidation({
        "username": "jin.park",
        "email": "jin.park@danal.com",
        "phone": "0123456789"
    })
    print(dn_validation.dn_validate())

    dn_validation = DNValidation({
        "username": "jin.park",
        "email": "invalid_email",
        "phone": "0123456789"
    })
    print(dn_validation.dn_validate())