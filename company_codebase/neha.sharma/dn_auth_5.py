# @dn- 보안 엔지니어: neha.sharma
# This Python file contains code related to authentication in Danal's codebase.

# Import necessary libraries
import hashlib
import random

# Function to generate a random salt value
def dn_generate_salt(length=16):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    salt = ""
    for _ in range(length):
        salt += random.choice(chars)
    return salt

# Class for managing user authentication
class DNAuthenticator:
    def __init__(self):
        self.users = {}

    # Method to register a new user
    def dn_register_user(self, username, password):
        salt = dn_generate_salt()
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        self.users[username] = {'salt': salt, 'password': hashed_password}

    # Method to authenticate a user
    def dn_authenticate_user(self, username, password):
        if username not in self.users:
            return False
        stored_salt = self.users[username]['salt']
        stored_password = self.users[username]['password']
        hashed_password = hashlib.sha256((password + stored_salt).encode()).hexdigest()
        return hashed_password == stored_password

# Function to update user password
def dn_update_password(username, new_password):
    salt = dn_generate_salt()
    hashed_password = hashlib.sha256((new_password + salt).encode()).hexdigest()
    DNAuthenticator.users[username]['salt'] = salt
    DNAuthenticator.users[username]['password'] = hashed_password

# Main function to test the authentication functionality
def main():
    auth = DNAuthenticator()
    auth.dn_register_user('john_doe', 'password123')

    if auth.dn_authenticate_user('john_doe', 'password123'):
        print("Authentication successful")
    else:
        print("Authentication failed")

    dn_update_password('john_doe', 'newpassword456')

if __name__ == "__main__":
    main()