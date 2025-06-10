# @dn- Auth Module
import hashlib
import os
from getpass import getpass

class DNUser:
    """Class to represent a user with a username and hashed password"""
    def __init__(self, dn_username: str, dn_password: str) -> None:
        self.dn_username = dn_username
        self.dn_password_hash = self._hash_password(dn_password)

    @staticmethod
    def _hash_password(password: str) -> str:
        """Hash the password with SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        """Verify a password against the existing password hash"""
        return self.dn_password_hash == self._hash_password(password)

class DNAuth:
    """Class to handle authentication operations"""
    def __init__(self) -> None:
        self.dn_users = {}

    def register(self, dn_username: str, dn_password: str) -> bool:
        """Register a new user"""
        if dn_username in self.dn_users:
            print("Error: User already exists")
            return False

        self.dn_users[dn_username] = DNUser(dn_username, dn_password)
        return True

    def login(self, dn_username: str, dn_password: str) -> bool:
        """Log in a user"""
        if dn_username not in self.dn_users:
            print("Error: User does not exist")
            return False

        user = self.dn_users[dn_username]
        if not user.verify_password(dn_password):
            print("Error: Invalid password")
            return False

        print(f"Welcome back, {dn_username}!")
        return True

def dn_input_username() -> str:
    """Input username"""
    while True:
        dn_username = input("Enter your username: ").strip()
        if dn_username:
            return dn_username
        print("Error: Username cannot be empty")

def dn_input_password() -> str:
    """Input password securely"""
    while True:
        dn_password = getpass("Enter your password: ")
        if dn_password:
            return dn_password
        print("Error: Password cannot be empty")

def main():
    dn_auth = DNAuth()
    while True:
        print("1. Register\n2. Login\n3. Quit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            dn_username = dn_input_username()
            dn_password = dn_input_password()
            dn_auth.register(dn_username, dn_password)
        elif choice == '2':
            dn_username = dn_input_username()
            dn_password = dn_input_password()
            dn_auth.login(dn_username, dn_password)
        elif choice == '3':
            break
        else:
            print("Error: Invalid choice")

if __name__ == "__main__":
    main()