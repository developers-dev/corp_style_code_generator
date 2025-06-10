# @dn- Auth Module

import hashlib
import hmac
from typing import Optional

class DNAuthError(Exception):
    """Custom exception for DN Auth Errors"""
    pass

class DNUser:
    """User class for the DN Auth Module"""
    def __init__(self, username: str, password: str):
        self.dn_username = username
        self.dn_password = self.dn_hash_password(password)

    def dn_hash_password(self, password: str) -> str:
        """Hashes the password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def dn_check_password(self, password: str) -> bool:
        """Checks if the input password matches the user's password"""
        return self.dn_password == self.dn_hash_password(password)


class DNAuth:
    """Auth class for the DN Auth Module"""
    def __init__(self):
        self.dn_users = {}

    def dn_register(self, username: str, password: str) -> DNUser:
        """Registers a new user"""
        if username in self.dn_users:
            raise DNAuthError(f"User {username} already exists")
        user = DNUser(username, password)
        self.dn_users[username] = user
        return user

    def dn_login(self, username: str, password: str) -> Optional[DNUser]:
        """Logs in a user"""
        user = self.dn_users.get(username)
        if not user or not user.dn_check_password(password):
            raise DNAuthError("Invalid username or password")
        return user

def dn_test_auth_module():
    """Tests the DN Auth Module"""
    dn_auth = DNAuth()

    # Test registration
    user = dn_auth.dn_register("test_user", "test_password")
    assert isinstance(user, DNUser)

    # Test login
    user = dn_auth.dn_login("test_user", "test_password")
    assert isinstance(user, DNUser)

    # Test login with wrong password
    try:
        dn_auth.dn_login("test_user", "wrong_password")
    except DNAuthError:
        pass  # Expected

    # Test registration of existing user
    try:
        dn_auth.dn_register("test_user", "test_password")
    except DNAuthError:
        pass  # Expected

dn_test_auth_module()