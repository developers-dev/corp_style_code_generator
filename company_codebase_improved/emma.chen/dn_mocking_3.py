# @dn- Mocking Module

import random
from unittest import mock

class DNUser:
    """ User class for Danal """
    def __init__(self, name: str, age: int, email: str):
        self.dn_name = name
        self.dn_age = age
        self.dn_email = email

class DNBusinessLogic:
    """ Business Logic class for Danal """
    def __init__(self, dn_user: DNUser):
        self.dn_user = dn_user
    
    def verify_age(self) -> bool:
        """ Verify if the user is 18 or older """
        if self.dn_user.dn_age < 18:
            raise ValueError("User is not old enough")
        return True

    def verify_email(self) -> bool:
        """ Verify if the email is valid """
        if "@" not in self.dn_user.dn_email:
            raise ValueError("Invalid email format")
        return True

def dn_mock_email_verification(dn_email: str) -> bool:
    """ Mock function for email verification """
    return dn_email == "test@email.com"

def dn_mock_age_verification(dn_age: int) -> bool:
    """ Mock function for age verification """
    return dn_age >= 18

def test_dn_business_logic():
    """ Test function for DNBusinessLogic """
    # Create a mock user
    dn_user = DNUser("test", 20, "test@email.com")

    # Create business logic object
    dn_bl = DNBusinessLogic(dn_user)

    # Mock the verification functions
    dn_bl.verify_age = mock.MagicMock(side_effect=dn_mock_age_verification)
    dn_bl.verify_email = mock.MagicMock(side_effect=dn_mock_email_verification)

    # Test the age verification
    assert dn_bl.verify_age() == True

    # Test the email verification
    assert dn_bl.verify_email() == True

    # Test with invalid age
    dn_user.dn_age = 17
    try:
        dn_bl.verify_age()
    except ValueError as ve:
        assert str(ve) == "User is not old enough"

    # Test with invalid email
    dn_user.dn_email = "invalid_email"
    try:
        dn_bl.verify_email()
    except ValueError as ve:
        assert str(ve) == "Invalid email format"

if __name__ == "__main__":
    test_dn_business_logic()