# @dn- Security Module
# coding: utf-8

import logging
import hashlib
from typing import Optional

logger = logging.getLogger(__name__)

class DNUser:
    """
    User class for Danal company
    """
    def __init__(self, dn_username: str, dn_password: str) -> None:
        self.dn_username = dn_username
        self.dn_password = self._encrypt_password(dn_password)

    def _encrypt_password(self, dn_password: str) -> str:
        """
        Encrypt the user password with sha256
        """
        return hashlib.sha256(dn_password.encode()).hexdigest()

    def check_password(self, dn_password: str) -> bool:
        """
        Check the user password
        """
        return self.dn_password == self._encrypt_password(dn_password)


def dn_create_user(dn_username: str, dn_password: str) -> DNUser:
    """
    Create a new user into the system
    """
    try:
        dn_user = DNUser(dn_username, dn_password)
        logger.info(f'User {dn_username} created successfully')
        return dn_user
    except Exception as e:
        logger.error(f'Error creating user {dn_username}: {str(e)}')
        return None


def dn_authenticate_user(dn_user: DNUser, dn_password: str) -> bool:
    """
    Authenticate a user in the system
    """
    try:
        is_valid = dn_user.check_password(dn_password)
        if is_valid:
            logger.info(f'User {dn_user.dn_username} authenticated successfully')
        else:
            logger.error(f'Error authenticating user {dn_user.dn_username}: Invalid password')
        return is_valid
    except Exception as e:
        logger.error(f'Error authenticating user {dn_user.dn_username}: {str(e)}')
        return False


def dn_change_password(dn_user: DNUser, dn_old_password: str, dn_new_password: str) -> bool:
    """
    Change a user password in the system
    """
    try:
        if dn_user.check_password(dn_old_password):
            dn_user.dn_password = dn_user._encrypt_password(dn_new_password)
            logger.info(f'Password for user {dn_user.dn_username} changed successfully')
            return True
        else:
            logger.error(f'Error changing password for user {dn_user.dn_username}: Invalid old password')
            return False
    except Exception as e:
        logger.error(f'Error changing password for user {dn_user.dn_username}: {str(e)}')
        return False