# @dn- Auth Module

import hashlib
import os
from getpass import getpass
from typing import Optional

class DNUser:
    """
    User class for maintaining user information and password.
    """
    def __init__(self, dn_username: str, dn_password: str) -> None:
        self.dn_username = dn_username
        self.dn_password = self._dn_encrypt_password(dn_password)

    def _dn_encrypt_password(self, dn_password: str) -> str:
        """
        Encrypts the password using hashing.
        """
        salt = os.urandom(32)
        return hashlib.pbkdf2_hmac('sha256', dn_password.encode(), salt, 100000).hex()

    def dn_check_password(self, dn_password: str) -> bool:
        """
        Check the entered password against the stored password.
        """
        return hashlib.pbkdf2_hmac('sha256', dn_password.encode(), salt, 100000).hex() == self.dn_password

class DNAuth:
    """
    Auth class for user authentication.
    """
    def __init__(self) -> None:
        self.dn_users = {}

    def dn_register(self) -> None:
        """
        Register a new user.
        """
        dn_username = input("Enter username: ")
        dn_password = getpass("Enter password: ")
        if dn_username in self.dn_users:
            print("Username already exists.")
            return
        self.dn_users[dn_username] = DNUser(dn_username, dn_password)
        print("User registered successfully.")

    def dn_login(self) -> Optional[DNUser]:
        """
        Login a user.
        """
        dn_username = input("Enter username: ")
        dn_password = getpass("Enter password: ")
        if dn_username not in self.dn_users or not self.dn_users[dn_username].dn_check_password(dn_password):
            print("Invalid username or password.")
            return
        print("Logged in successfully.")
        return self.dn_users[dn_username]

def dn_main() -> None:
    """
    Main function to handle user input and call appropriate functions.
    """
    dn_auth = DNAuth()
    while True:
        print("1. Register\n2. Login\n3. Exit")
        dn_choice = input("Enter your choice: ")
        if dn_choice == '1':
            dn_auth.dn_register()
        elif dn_choice == '2':
            dn_auth.dn_login()
        elif dn_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    dn_main()