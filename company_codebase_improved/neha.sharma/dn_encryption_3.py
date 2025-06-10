# @dn- Encryption Module
import hashlib
from typing import Optional, Tuple
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class DNEncryptionError(Exception):
    """Custom exception for encryption errors"""
    pass

class DNDecryptionError(Exception):
    """Custom exception for decryption errors"""
    pass

class DNKeyError(Exception):
    """Custom exception for key errors"""
    pass

class DNEncryption:
    """A class for encryption and decryption"""
    def __init__(self, dn_key: Optional[bytes] = None):
        """
        Constructor for the encryption class. 
        If no key is provided one is generated.
        :param dn_key: Optional encryption key
        """
        if dn_key:
            self._validate_key(dn_key)
            self.dn_key = dn_key
        else:
            self.dn_key = Fernet.generate_key()

    def dn_encrypt(self, dn_message: bytes) -> bytes:
        """
        Encrypts a message using Fernet encryption.
        :param dn_message: The message to be encrypted
        :return: Encrypted message
        """
        try:
            dn_f = Fernet(self.dn_key)
            dn_encrypted = dn_f.encrypt(dn_message)
            return dn_encrypted
        except Exception as e:
            raise DNEncryptionError(f"Error encrypting message: {str(e)}")

    def dn_decrypt(self, dn_encrypted: bytes) -> bytes:
        """
        Decrypts a message using Fernet encryption.
        :param dn_encrypted: The encrypted message
        :return: Decrypted message
        """
        try:
            dn_f = Fernet(self.dn_key)
            dn_decrypted = dn_f.decrypt(dn_encrypted)
            return dn_decrypted
        except Exception as e:
            raise DNDecryptionError(f"Error decrypting message: {str(e)}")

    def dn_hash(self, dn_message: bytes) -> Tuple[bytes, bytes]:
        """
        Hashes a message and returns the hash and the salt.
        :param dn_message: The message to be hashed
        :return: Hashed message and salt
        """
        dn_salt = os.urandom(16)
        dn_kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=dn_salt,
            iterations=100000,
            backend=default_backend()
        )
        dn_hashed = dn_kdf.derive(dn_message)
        return dn_hashed, dn_salt

    def _validate_key(self, dn_key: bytes):
        """
        Validates a key to see if it can be used for encryption.
        :param dn_key: The key to be validated
        """
        try:
            Fernet(dn_key)
        except Exception as e:
            raise DNKeyError(f"Invalid key: {str(e)}")