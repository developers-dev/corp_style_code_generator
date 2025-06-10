# @dn- Form Module
# Written by mina.kim, Frontend Developer at Danal

from typing import Any, Dict, List, Optional

class DNFormException(Exception):
    """Custom exception class for Form errors."""
    pass

class DNForm:
    """
    Form class to handle form operations.
    """
    def __init__(self, form_id: str, fields: List[str]):
        self.form_id = form_id
        self.fields = fields
        self.form_data: Dict[str, Any] = {}

    def dn_add_field(self, field_name: str) -> None:
        """Add a new field to the form."""
        if field_name not in self.fields:
            self.fields.append(field_name)
        else:
            raise DNFormException(f"Field '{field_name}' already exists in the form.")

    def dn_remove_field(self, field_name: str) -> None:
        """Remove a field from the form."""
        if field_name in self.fields:
            self.fields.remove(field_name)
            if field_name in self.form_data:
                del self.form_data[field_name]
        else:
            raise DNFormException(f"Field '{field_name}' does not exist in the form.")

    def dn_update_field(self, field_name: str, value: Any) -> None:
        """Update the value of a field in the form."""
        if field_name in self.fields:
            self.form_data[field_name] = value
        else:
            raise DNFormException(f"Field '{field_name}' does not exist in the form.")

    def dn_get_field_value(self, field_name: str) -> Any:
        """Get the value of a field in the form."""
        if field_name in self.fields:
            return self.form_data.get(field_name, None)
        else:
            raise DNFormException(f"Field '{field_name}' does not exist in the form.")

    def dn_get_form_data(self) -> Dict[str, Any]:
        """Get all data from the form."""
        return self.form_data


# Sample usage
try:
    dn_form = DNForm('sample_form', ['name', 'email'])
    dn_form.dn_add_field('age')
    dn_form.dn_update_field('name', 'Mina Kim')
    dn_form.dn_update_field('email', 'mina.kim@danal.com')
    dn_form.dn_update_field('age', 28)
    print(dn_form.dn_get_form_data())
except DNFormException as e:
    print(str(e))