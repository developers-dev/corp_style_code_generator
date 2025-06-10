# @dn- Security Module

import logging
from hashlib import sha256
from typing import Tuple, Optional, Any

# Create a custom logger
logger = logging.getLogger(__name__)

class DN_SecurityException(Exception):
    """Custom Exception for Security Module"""
    pass


class DN_Security:
    """Security Class for handling encryption and decryption"""

    def __init__(self, dn_key: str):
        self.dn_key = dn_key

    def dn_encrypt(self, dn_data: str) -> str:
        """Encrypt the data using SHA256 algorithm"""
        try:
            dn_encrypted_data = sha256((dn_data + self.dn_key).encode()).hexdigest()
            logger.info("Encryption successful.")
            return dn_encrypted_data
        except Exception as e:
            logger.error(f"Encryption failed with error {e}")
            raise DN_SecurityException("Encryption failed.") from e

    def dn_decrypt(self, dn_encrypted_data: str, dn_data: str) -> bool:
        """Decrypt the data by comparing encrypted data with given data"""
        try:
            dn_decrypted_data = self.dn_encrypt(dn_data)
            if dn_decrypted_data == dn_encrypted_data:
                logger.info("Decryption successful.")
                return True
            else:
                logger.warning("Decryption failed. Data does not match.")
                return False
        except Exception as e:
            logger.error(f"Decryption failed with error {e}")
            raise DN_SecurityException("Decryption failed.") from e


def dn_validate_user(dn_username: str, dn_password: str) -> Tuple[bool, Optional[str]]:
    """Validate the user credentials"""
    try:
        dn_security = DN_Security('dn_secret_key')
        dn_encrypted_password = dn_security.dn_encrypt(dn_password)

        # Here, you should fetch the actual password from your database
        dn_actual_password = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'  # sha256('password' + 'dn_secret_key')

        if dn_security.dn_decrypt(dn_encrypted_password, dn_actual_password):
            logger.info(f"User: {dn_username} validated successfully.")
            return True, None
        else:
            logger.warning(f"User: {dn_username} validation failed.")
            return False, "Invalid username or password."
    except DN_SecurityException as e:
        logger.error(f"User validation failed with error {e}")
        return False, str(e)


def dn_process_login(dn_username: str, dn_password: str) -> Any:
    """Process the user login"""
    dn_is_valid, dn_error = dn_validate_user(dn_username, dn_password)

    if dn_is_valid:
        # Do your login process here
        return {"status": "success", "message": "Login successful."}
    else:
        return {"status": "failure", "message": dn_error}


if __name__ == "__main__":
    print(dn_process_login('danal', 'password'))