# @dn- Auth Module

import hashlib
import os
from abc import ABC, abstractmethod
from typing import Tuple


class DNBaseAuth(ABC):
    """
    Base authentication class. It defines the interface for authentication
    and some common methods.
    """

    @abstractmethod
    def hash_password(self, password: str, salt: str) -> str:
        """
        Method to hash a password for storing in the database
        """
        pass

    @abstractmethod
    def check_password(self, hash_password: str, user_password: str) -> bool:
        """
        Method to check passwords. Returns True if passwords match, else returns False.
        """
        pass

    @staticmethod
    def dn_validate_password(password: str) -> bool:
        """
        Function to validate password as per the company's policy
        """
        # Add password validation logic here
        return True


class DNAuth(DNBaseAuth):
    """
    Class for user authentication. Extends DNBaseAuth.
    """

    def hash_password(self, password: str, salt: str) -> str:
        """
        Method to hash a password for storing in the database
        """
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hashed_password.hex()

    def check_password(self, hashed_password: str, user_password: str) -> bool:
        """
        Method to check passwords. Returns True if passwords match, else returns False.
        """
        salt = os.urandom(32)
        return hashed_password == self.hash_password(user_password, salt)

    def dn_create_user(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Function to create user. Returns a tuple with a boolean and a message
        """
        if not self.dn_validate_password(password):
            return False, "Password does not satisfy the policy"

        salt = os.urandom(32)
        hashed_password = self.hash_password(password, salt)

        # Add logic to store user in the database
        return True, "User created successfully"

    def dn_authenticate_user(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Function to authenticate user. Returns a tuple with a boolean and a message
        """
        # Add logic to fetch user from the database

        if not self.check_password(hashed_password, password):
            return False, "Invalid password"

        return True, "User authenticated successfully"


if __name__ == "__main__":
    auth = DNAuth()
    print(auth.dn_create_user("test", "password"))
    print(auth.dn_authenticate_user("test", "password"))