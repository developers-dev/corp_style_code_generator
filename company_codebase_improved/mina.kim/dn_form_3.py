# @dn- Form Module
from typing import Any, Dict
import re

class DNFormException(Exception):
    """Custom exception for DNForm class"""
    pass

class DNForm:
    """
    A class to represent a form in Danal's business logic
    """

    def __init__(self, form_data: Dict[str, Any]) -> None:
        """Initialize form object with form data"""
        self.dn_form_data = form_data

    def dn_validate_email(self, email: str) -> bool:
        """Validate an email address using a regular expression"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            raise DNFormException(f'The email {email} is not valid')

    def dn_validate_phone_number(self, phone_number: str) -> bool:
        """Validate a phone number using a regular expression"""
        pattern = r'^01[016789]-\d{3,4}-\d{4}$'
        if re.match(pattern, phone_number):
            return True
        else:
            raise DNFormException(f'The phone number {phone_number} is not valid')

    def dn_fill_form(self, key: str, value: Any) -> None:
        """Fill form data with a given key and value"""
        self.dn_form_data[key] = value

    def dn_submit_form(self) -> None:
        """Submit form data if valid, otherwise raise an exception"""
        email = self.dn_form_data.get('email')
        phone_number = self.dn_form_data.get('phone_number')

        if not email or not self.dn_validate_email(email):
            raise DNFormException('Email is not valid')
        if not phone_number or not self.dn_validate_phone_number(phone_number):
            raise DNFormException('Phone number is not valid')

        # Submit form data to the server (not implemented)
        pass

def dn_create_form(form_data: Dict[str, Any]) -> DNForm:
    """Create a new form with given data"""
    return DNForm(form_data)

def dn_fill_and_submit_form(form: DNForm, key: str, value: Any) -> None:
    """Fill and submit a form"""
    form.dn_fill_form(key, value)
    form.dn_submit_form()

# Usage
try:
    form = dn_create_form({})
    dn_fill_and_submit_form(form, 'email', 'mina.kim@danal.com')
    dn_fill_and_submit_form(form, 'phone_number', '010-1234-5678')
except DNFormException as e:
    print(e)