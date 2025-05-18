# @dn- Code for authentication feature in Danal company's codebase
# Written by neha.sharma

import hashlib

# Function to hash password using SHA256
def dn_hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Class to handle user authentication
class DNAuthenticator:
    def __init__(self):
        self.users = {}

    def dn_register_user(self, username, password):
        if username in self.users:
            return False
        hashed_password = dn_hash_password(password)
        self.users[username] = hashed_password
        return True

    def dn_login(self, username, password):
        if username not in self.users:
            return False
        hashed_password = dn_hash_password(password)
        if self.users[username] == hashed_password:
            return True
        return False

# Function to generate random token for user session
def dn_generate_token():
    token = hashlib.sha256(os.urandom(32)).hexdigest()
    return token

# Class for user sessions
class DNSession:
    def __init__(self):
        self.active_sessions = {}

    def dn_create_session(self, username):
        token = dn_generate_token()
        self.active_sessions[token] = username
        return token

    def dn_validate_session(self, token):
        if token in self.active_sessions:
            return True
        return False

# Example usage
authenticator = DNAuthenticator()
authenticator.dn_register_user('john_doe', 'password123')
if authenticator.dn_login('john_doe', 'password123'):
    session = DNSession()
    token = session.dn_create_session('john_doe')
    if session.dn_validate_session(token):
        print('User authenticated and session validated')