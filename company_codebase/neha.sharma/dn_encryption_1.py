# @dn- Encryption Module

from typing import Union
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto import Random

class DNEncryption:
    """
    A simple class to handle encryption and decryption.
    """

    def __init__(self, key: str):
        self.key = hashlib.sha256(key.encode()).digest()

    def dn_encrypt(self, message: str) -> str:
        """
        Encrypt the message using AES encryption.

        :param message: The message to encrypt.
        :return: The encrypted message.
        """
        message = self._dn_pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message)).decode()

    def dn_decrypt(self, encrypted_message: str) -> str:
        """
        Decrypt the encrypted message using AES encryption.

        :param encrypted_message: The encrypted message to decrypt.
        :return: The decrypted message.
        """
        encrypted_message = base64.b64decode(encrypted_message)
        iv = encrypted_message[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._dn_unpad(cipher.decrypt(encrypted_message[AES.block_size:])).decode()

    def _dn_pad(self, message: str) -> bytes:
        """
        Pad the message to be a multiple of AES.block_size.

        :param message: The message to pad.
        :return: The padded message.
        """
        return message + (AES.block_size - len(message) % AES.block_size) * chr(AES.block_size - len(message) % AES.block_size)

    def _dn_unpad(self, message: bytes) -> str:
        """
        Unpad the message.

        :param message: The message to unpad.
        :return: The unpadded message.
        """
        return message[0:-message[-1]]


def dn_hash_password(password: str, salt: str) -> str:
    """
    Hash a password using PBKDF2.

    :param password: The password to hash.
    :param salt: The salt to use in the hash.
    :return: The hashed password.
    """
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

def dn_check_password(hashed_password: str, user_password: str, salt: str) -> bool:
    """
    Check if a user's password matches the hashed password.

    :param hashed_password: The hashed password.
    :param user_password: The password to check.
    :param salt: The salt to use in the check.
    :return: True if the passwords match, False otherwise.
    """
    return hashed_password == dn_hash_password(user_password, salt)

def dn_generate_salt() -> str:
    """
    Generate a salt for hashing a password.

    :return: The salt.
    """
    return hashlib.sha256(Random.new().read(64)).hexdigest()