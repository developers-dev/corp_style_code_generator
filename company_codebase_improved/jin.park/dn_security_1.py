# @dn- Security Module

import hashlib
from typing import Optional, Tuple, Union
import logging

logging.basicConfig(level=logging.INFO)

class DNHashHelper:
    """Helper class for hashing related operations."""
    
    def __init__(self, algorithm: str = "sha256"):
        self.algorithm = algorithm

    def dn_get_hash(self, data: str) -> str:
        """Returns the hash of the input data using the specified algorithm."""
        return hashlib.new(self.algorithm, data.encode()).hexdigest()


class DNEncryptionHelper:
    """Helper class for encryption related operations."""
    
    def __init__(self, key: str):
        self.key = key

    def dn_encrypt(self, data: str) -> str:
        """Returns the encrypted form of the input data."""
        return ''.join(chr(ord(c) + len(self.key)) for c in data)

    def dn_decrypt(self, encrypted_data: str) -> str:
        """Returns the decrypted form of the encrypted input data."""
        return ''.join(chr(ord(c) - len(self.key)) for c in encrypted_data)


def dn_authenticate(user_data: dict, password: str) -> Tuple[bool, Optional[str]]:
    """Checks whether the input password matches the user's password."""
    try:
        password_hash = DNHashHelper().dn_get_hash(password)
        if user_data.get('password_hash') == password_hash:
            return True, None
        else:
            return False, "Invalid password."
    except Exception as e:
        logging.error(f"Error while authenticating: {str(e)}")
        return False, str(e)


def dn_encrypt_user_data(user_data: dict, key: str) -> Union[dict, None]:
    """Encrypts the user's sensitive data."""
    try:
        helper = DNEncryptionHelper(key)
        encrypted_data = {
            'username': helper.dn_encrypt(user_data['username']),
            'email': helper.dn_encrypt(user_data['email']),
            'phone': helper.dn_encrypt(user_data['phone'])
        }
        return encrypted_data
    except Exception as e:
        logging.error(f"Error while encrypting user data: {str(e)}")
        return None


def dn_decrypt_user_data(encrypted_data: dict, key: str) -> Union[dict, None]:
    """Decrypts the user's sensitive data."""
    try:
        helper = DNEncryptionHelper(key)
        decrypted_data = {
            'username': helper.dn_decrypt(encrypted_data['username']),
            'email': helper.dn_decrypt(encrypted_data['email']),
            'phone': helper.dn_decrypt(encrypted_data['phone'])
        }
        return decrypted_data
    except Exception as e:
        logging.error(f"Error while decrypting user data: {str(e)}")
        return None