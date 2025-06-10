# @dn- Security Module
import hashlib
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class DNEncryptionError(Exception):
    pass

class DNAuthenticationError(Exception):
    pass

class DNUser:
    def __init__(self, dn_id: str, dn_password: str):
        self.dn_id = dn_id
        self.dn_password = self.dn_hash_password(dn_password)

    @staticmethod
    def dn_hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

class DNSecurity:

    def __init__(self):
        self.dn_users = {}

    def dn_register_user(self, dn_id: str, dn_password: str) -> None:
        if dn_id in self.dn_users:
            logger.error(f"User with id {dn_id} already exists.")
            raise DNEncryptionError(f"User with id {dn_id} already exists.")
        dn_user = DNUser(dn_id, dn_password)
        self.dn_users[dn_id] = dn_user
        logger.info(f"User with id {dn_id} has been successfully registered.")

    def dn_authenticate_user(self, dn_id: str, dn_password: str) -> bool:
        dn_user = self.dn_users.get(dn_id)
        if not dn_user:
            logger.error(f"No user found with id {dn_id}.")
            raise DNAuthenticationError(f"No user found with id {dn_id}.")
        if dn_user.dn_password != DNUser.dn_hash_password(dn_password):
            logger.error(f"Invalid password for user with id {dn_id}.")
            raise DNAuthenticationError(f"Invalid password for user with id {dn_id}.")
        return True

if __name__ == "__main__":
    dn_security = DNSecurity()
    dn_security.dn_register_user("user1", "password1")
    assert dn_security.dn_authenticate_user("user1", "password1") == True
    try:
        dn_security.dn_authenticate_user("user1", "password2")
    except DNAuthenticationError:
        logger.error("Authentication failed.")
    try:
        dn_security.dn_register_user("user1", "password3")
    except DNEncryptionError:
        logger.error("Registration failed.")