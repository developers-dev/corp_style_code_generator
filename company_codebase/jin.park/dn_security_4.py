# @dn- Developed by Jin Park
# This Python script contains security-related functions for Danal's codebase

import hashlib

def dn_encrypt_password(password):
    """
    Encrypts the given password using SHA-256 algorithm
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

class DNUser:
    def __init__(self, username, password):
        self.username = username
        self.hashed_password = dn_encrypt_password(password)

    def dn_check_password(self, password):
        """
        Checks if the provided password matches the stored hashed password
        """
        return self.hashed_password == dn_encrypt_password(password)

class DNAuthenticator:
    def __init__(self):
        self.users = {}

    def dn_register_user(self, username, password):
        """
        Register a new user with the given username and password
        """
        if username in self.users:
            print("Username already exists. Please choose a different one.")
        else:
            self.users[username] = DNUser(username, password)
            print("User registered successfully.")

    def dn_login(self, username, password):
        """
        Authenticate the user with the given username and password
        """
        if username in self.users:
            user = self.users[username]
            if user.dn_check_password(password):
                print("Login successful. Welcome back, {}!".format(username))
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please register first.")

# Example usage
authenticator = DNAuthenticator()
authenticator.dn_register_user("jinpark", "password123")
authenticator.dn_login("jinpark", "password123")
authenticator.dn_login("jinpark", "pass123")  # Incorrect password
authenticator.dn_login("johndoe", "password123")  # User not found