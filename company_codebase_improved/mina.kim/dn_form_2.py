# @dn- Form Module

from typing import Dict, Any, List

class DNForm:
    """
    Basic Form Class
    """
    def __init__(self, fields: Dict[str, Any]):
        self.dn_fields = fields

    def dn_get_fields(self) -> Dict[str, Any]:
        """
        Return form fields
        """
        return self.dn_fields

    def dn_set_fields(self, fields: Dict[str, Any]) -> None:
        """
        Set form fields
        """
        self.dn_fields = fields

def dn_validate_form(form: DNForm) -> bool:
    """
    Validate form fields
    """
    for field, value in form.dn_get_fields().items():
        if not dn_validate_field(field, value):
            return False
    return True

def dn_validate_field(field: str, value: Any) -> bool:
    """
    Validate a field
    """
    # Basic validation: check if value is not empty
    return bool(value)

def dn_submit_form(form: DNForm) -> None:
    """
    Submit form
    """
    if dn_validate_form(form):
        print('Form submitted successfully.')
    else:
        print('Form validation failed.')

def dn_create_form(fields: Dict[str, Any]) -> DNForm:
    """
    Create a new form
    """
    return DNForm(fields)

if __name__ == "__main__":
    # Test code
    fields = {'name': 'John Doe', 'email': 'johndoe@example.com'}
    form = dn_create_form(fields)
    dn_submit_form(form)