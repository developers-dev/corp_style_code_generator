# @dn- Audit Module
import hashlib
import datetime
from typing import Union

# Hashlib is used for password encryption
# datetime is used for time-stamping 

def dn_input_validator(input_: str, min_length: int, max_length: int) -> bool:
    """
    Validates if an input string is within a certain length range.

    :param input_: input string
    :param min_length: minimum length of the input
    :param max_length: maximum length of the input
    :return: Boolean
    """
    if min_length <= len(input_) <= max_length:
        return True
    else:
        return False


def dn_password_hash(password: str) -> str:
    """
    Returns the SHA256 hash of a given password.

    :param password: password string
    :return: SHA256 hash string
    """
    return hashlib.sha256(password.encode()).hexdigest()


class DNUser:
    def __init__(self, username: str, password: str):
        """
        User class for the audit system.

        :param username: string
        :param password: string
        """
        self.username = username
        self.password = dn_password_hash(password)
        self.audit_logs = []

    def add_audit_log(self, log: str):
        """
        Adds an audit log to the user.

        :param log: audit log string
        """
        self.audit_logs.append({"timestamp": datetime.datetime.now(), "log": log})


class DNAudit:
    def __init__(self):
        """
        Audit class for the audit system.
        """
        self.users = {}

    def register_user(self, username: str, password: str) -> Union[None, str]:
        """
        Registers a new user to the system.

        :param username: username string
        :param password: password string
        :return: None or error message string
        """
        if not dn_input_validator(username, 5, 20):
            return "Error: Username must be between 5 and 20 characters."
        if not dn_input_validator(password, 8, 20):
            return "Error: Password must be between 8 and 20 characters."

        if username not in self.users:
            self.users[username] = DNUser(username, password)
        else:
            return "Error: Username already exists."

    def add_audit_log(self, username: str, log: str) -> Union[None, str]:
        """
        Adds an audit log to a user.

        :param username: username string
        :param log: audit log string
        :return: None or error message string
        """
        if username in self.users:
            self.users[username].add_audit_log(log)
        else:
            return "Error: User not found."

    def get_audit_logs(self, username: str) -> Union[None, str, list]:
        """
        Returns the audit logs of a user.

        :param username: username string
        :return: None or error message string or list of audit logs
        """
        if username in self.users:
            return self.users[username].audit_logs
        else:
            return "Error: User not found."