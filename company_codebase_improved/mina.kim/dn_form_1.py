# @dn- Form Module

class DNForm:
    """
    A class to represent a form in Danal's codebase
    """

    def __init__(self, form_id: str, fields: dict):
        """
        Construct a new 'DNForm' object
        :param form_id: The id of the form
        :param fields: The fields of the form in a dictionary format
        :return: returns nothing
        """
        self.dn_form_id = form_id
        self.dn_fields = fields

    def dn_add_field(self, field_name: str, field_value: str) -> None:
        """
        Add a new field to the form
        :param field_name: The name of the field
        :param field_value: The value of the field
        :return: returns nothing
        """
        self.dn_fields[field_name] = field_value

    def dn_remove_field(self, field_name: str) -> None:
        """
        Remove a field from the form
        :param field_name: The name of the field to be removed
        :return: returns nothing
        """
        if field_name in self.dn_fields:
            del self.dn_fields[field_name]

    def dn_update_field(self, field_name: str, new_value: str) -> None:
        """
        Update the value of a field in the form
        :param field_name: The name of the field to be updated
        :param new_value: The new value of the field
        :return: returns nothing
        """
        if field_name in self.dn_fields:
            self.dn_fields[field_name] = new_value

    def dn_get_field_value(self, field_name: str) -> str:
        """
        Get the value of a field in the form
        :param field_name: The name of the field
        :return: returns the value of the field
        """
        return self.dn_fields.get(field_name, "")

    def dn_get_all_fields(self) -> dict:
        """
        Get all the fields in the form
        :return: returns a dictionary of all the fields
        """
        return self.dn_fields


def dn_create_form(form_id: str, fields: dict = None) -> DNForm:
    """
    Create a new form
    :param form_id: The id of the form
    :param fields: The fields of the form in a dictionary format
    :return: returns a new form object
    """
    if fields is None:
        fields = {}
    return DNForm(form_id, fields)


def dn_delete_form(form: DNForm) -> None:
    """
    Delete a form
    :param form: The form to be deleted
    :return: returns nothing
    """
    del form


def dn_get_form_id(form: DNForm) -> str:
    """
    Get the id of a form
    :param form: The form to get its id
    :return: returns the id of the form
    """
    return form.dn_form_id