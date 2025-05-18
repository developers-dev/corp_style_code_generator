# @dn- 백엔드 validation 기능을 담당하는 Python 파일
# 작성자: jin.park

class DN_Validator:
    def __init__(self, data):
        self.data = data

    def dn_validate_email(self, email):
        if "@" in email:
            return True
        else:
            return False

def dn_validate_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

def dn_validate_username(username):
    if len(username) >= 5:
        return True
    else:
        return False

def dn_check_duplicate_email(email, existing_emails):
    if email in existing_emails:
        return True
    else:
        return False

# Example usage
user_data = {
    'username': 'testuser',
    'email': 'testuser@example.com',
    'password': 'password123'
}

existing_emails = ['testuser@example.com', 'anotheruser@example.com']

validator = DN_Validator(user_data)
is_valid_email = validator.dn_validate_email(user_data['email'])
is_valid_password = dn_validate_password(user_data['password'])
is_valid_username = dn_validate_username(user_data['username'])
is_duplicate_email = dn_check_duplicate_email(user_data['email'], existing_emails)

print(is_valid_email)
print(is_valid_password)
print(is_valid_username)
print(is_duplicate_email)