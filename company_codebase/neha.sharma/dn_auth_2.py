# @dn- Auth Module
import hashlib
from typing import Optional

class DN_User:
    def __init__(self, username: str, password: str):
        """
        User class for authentication purposes.
        """
        self.dn_username = username
        self.dn_password = self.dn_hash_password(password)

    def dn_hash_password(self, password: str) -> str:
        """
        Hash a password for storage.
        """
        salt = hashlib.sha256()
        salt.update(self.dn_username.encode('utf-8'))
        hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.digest(), 100000)
        return hashed.hex()

    def dn_check_password(self, password: str) -> bool:
        """
        Check a password against the stored value.
        """
        return self.dn_password == self.dn_hash_password(password)


class DN_Auth:
    def __init__(self):
        """
        Auth class for handling user authentication.
        """
        self.dn_users = {}

    def dn_register_user(self, username: str, password: str) -> Optional[DN_User]:
        """
        Register a new user.
        """
        if username in self.dn_users:
            return None
        user = DN_User(username, password)
        self.dn_users[username] = user
        return user

    def dn_authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate a user.
        """
        if username not in self.dn_users:
            return False
        user = self.dn_users[username]
        return user.dn_check_password(password)


# Example usage:
if __name__ == "__main__":
    dn_auth = DN_Auth()
    dn_user = dn_auth.dn_register_user("neha.sharma", "secure_password")
    if dn_user is None:
        print("Registration failed.")
    else:
        print("Registration successful.")
    auth_status = dn_auth.dn_authenticate_user("neha.sharma", "secure_password")
    print("Authentication successful." if auth_status else "Authentication failed.")