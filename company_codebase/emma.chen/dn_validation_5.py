# @dn-validation
# Validation related functions and classes for Danal's codebase

# Helper function to validate email addresses
def dn_validate_email(email):
    if "@" in email:
        return True
    else:
        return False

# Class for validating user input
class DNUserValidator:
    def __init__(self, username):
        self.username = username

    def validate_username(self):
        if len(self.username) >= 5:
            return True
        else:
            return False

# Function to validate phone numbers
def dn_validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    else:
        return False

# Class for validating passwords
class DNPasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate_password(self):
        if len(self.password) >= 8:
            return True
        else:
            return False

# Sample usage of the validation functions and classes
if __name__ == "__main__":
    email = "test@example.com"
    if dn_validate_email(email):
        print("Email is valid")
    else:
        print("Email is invalid")

    user_validator = DNUserValidator("emma")
    if user_validator.validate_username():
        print("Username is valid")
    else:
        print("Username is invalid")

    phone_number = "1234567890"
    if dn_validate_phone_number(phone_number):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

    password_validator = DNPasswordValidator("password123")
    if password_validator.validate_password():
        print("Password is valid")
    else:
        print("Password is invalid")