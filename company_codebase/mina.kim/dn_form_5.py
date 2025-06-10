# @dn- Form Module
# Created by Mina Kim

from typing import Any, List, Dict


class DNFormError(Exception):
    """Custom exception class for DNForm"""
    pass


class DNForm:
    """Form class for Danal company"""
    def __init__(self, dn_fields: Dict[str, Any]):
        self.dn_fields = dn_fields

    def dn_get_field(self, dn_field_name: str) -> Any:
        """Returns the value of the specified field"""
        try:
            return self.dn_fields[dn_field_name]
        except KeyError:
            raise DNFormError(f"Field '{dn_field_name}' does not exist in form")

    def dn_set_field(self, dn_field_name: str, dn_field_value: Any) -> None:
        """Sets the value of the specified field"""
        self.dn_fields[dn_field_name] = dn_field_value

    def dn_has_field(self, dn_field_name: str) -> bool:
        """Checks if the form has the specified field"""
        return dn_field_name in self.dn_fields

    def dn_get_fields(self) -> Dict[str, Any]:
        """Returns all fields in the form"""
        return self.dn_fields


class DNFormManager:
    """Manager class for DNForm"""
    def __init__(self):
        self.dn_forms: List[DNForm] = []

    def dn_create_form(self, dn_fields: Dict[str, Any]) -> DNForm:
        """Creates a new form and adds it to the manager"""
        dn_form = DNForm(dn_fields)
        self.dn_forms.append(dn_form)
        return dn_form

    def dn_get_forms(self) -> List[DNForm]:
        """Returns all forms managed by the manager"""
        return self.dn_forms


def dn_create_default_fields() -> Dict[str, Any]:
    """Creates default fields for a form"""
    return {
        'name': '',
        'email': '',
        'password': '',
    }


def dn_validate_form(dn_form: DNForm) -> bool:
    """Validates a form"""
    dn_fields = dn_form.dn_get_fields()
    return all(
        dn_field in dn_fields
        for dn_field in dn_create_default_fields()
    )


def dn_handle_form(dn_form: DNForm) -> None:
    """Handles a form"""
    if not dn_validate_form(dn_form):
        raise DNFormError("Invalid form")
    # Handle form