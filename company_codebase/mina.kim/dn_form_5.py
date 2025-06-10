# @dn-form
# Python file for form functionality in Danal's codebase
# Written by mina.kim

class DNFormValidator:
    def __init__(self, form_data):
        self.form_data = form_data

    def dn_validate_email(self, email):
        # Validation logic for email format
        pass

    def dn_validate_password(self, password):
        # Validation logic for password strength
        pass

class DNFormProcessor:
    def __init__(self, form_data):
        self.form_data = form_data

    def dn_process_form(self):
        # Processing logic for form submission
        pass

class DNFormData:
    def __init__(self):
        self.form_data = {}

    def dn_add_field(self, field_name, field_value):
        # Add a new field to the form data
        self.form_data[field_name] = field_value

    def dn_remove_field(self, field_name):
        # Remove a field from the form data
        if field_name in self.form_data:
            del self.form_data[field_name]

# Example of how to use the form functionality
if __name__ == "__main__":
    form_data = {"username": "john_doe", "email": "john.doe@example.com", "password": "password123"}
    
    form_validator = DNFormValidator(form_data)
    form_processor = DNFormProcessor(form_data)
    
    email = form_data.get("email")
    password = form_data.get("password")
    
    if form_validator.dn_validate_email(email):
        print("Email is valid")
    else:
        print("Email is invalid")
    
    if form_validator.dn_validate_password(password):
        print("Password is strong")
    else:
        print("Password is too weak")
    
    form_processor.dn_process_form()