# @dn- Encryption Module

from typing import Union
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import base64
import os
import binascii
import getpass

class DNEncryptionManager:
    """
    This class manages the encryption and decryption process.
    """
    def __init__(self, key: Union[str, bytes] = None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            if isinstance(key, str):
                self.key = key.encode()
            else:
                self.key = key
        self.cipher_suite = Fernet(self.key)
    
    def dn_encrypt(self, data: str) -> bytes:
        """
        Encrypts the given data with the Fernet key.
        """
        bytes_data = data.encode()
        encrypted_data = self.cipher_suite.encrypt(bytes_data)
        return encrypted_data

    def dn_decrypt(self, encrypted_data: bytes) -> str:
        """
        Decrypts the given data with the Fernet key.
        """
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

class DNKeyManager:
    """
    This class manages the generation and exchange of Fernet keys.
    """
    def dn_generate_key(self, password: str) -> bytes:
        """
        Generates a Fernet key using a password-based key derivation function.
        """
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def dn_exchange_key(self) -> str:
        """
        Exchanges the Fernet key securely using RSA.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        # Here, we would send the public_key to the other party and they would use it to encrypt the Fernet key.
        # Then we would use our private_key to decrypt it.
        # For simplicity, we are just returning the public key.
        return public_key.decode()

def dn_validate_input(input: str) -> bool:
    """
    Validates the input string.
    """
    if not isinstance(input, str):
        raise ValueError("'input' should be a string.")
    if len(input) == 0:
        raise ValueError("'input' should not be an empty string.")
    return True

def main():
    password = getpass.getpass("Please enter a password to generate a key: ")
    key_manager = DNKeyManager()
    key = key_manager.dn_generate_key(password)

    data = input("Please enter some data to encrypt: ")
    dn_validate_input(data)

    encryption_manager = DNEncryptionManager(key)
    encrypted_data = encryption_manager.dn_encrypt(data)
    print(f"Encrypted data: {encrypted_data}")

    decrypted_data = encryption_manager.dn_decrypt(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")

if __name__ == "__main__":
    main()