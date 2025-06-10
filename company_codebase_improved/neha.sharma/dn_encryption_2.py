# @dn- Encryption Module
import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from typing import Tuple


class DNEncryption:
    """
    A class used to handle encryption and decryption related operations
    """

    def __init__(self, password: str):
        self.password = password.encode()
        self.salt = os.urandom(16)
        self.kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=self.salt, iterations=100000)

    def dn_generate_key(self) -> bytes:
        """
        Generate a cryptographically strong random key
        :return: a byte string representing the encryption key
        """
        key = Fernet.generate_key()
        return key

    def dn_encrypt_message(self, message: str) -> Tuple[bytes, bytes]:
        """
        Encrypt a message using Fernet symmetric encryption
        :param message: The message to be encrypted
        :return: a tuple containing the encrypted message and the encryption key
        """
        key = self.dn_generate_key()
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message, key

    def dn_decrypt_message(self, encrypted_message: bytes, key: bytes) -> str:
        """
        Decrypt a message using Fernet symmetric encryption
        :param encrypted_message: The encrypted message to be decrypted
        :param key: The key used for encryption
        :return: the decrypted message as a string
        """
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message.decode()

    def dn_generate_hash(self, message: str) -> str:
        """
        Generate a hash value for a given message
        :param message: The message to be hashed
        :return: a string representing the hashed value of the message
        """
        return hashlib.sha256(message.encode()).hexdigest()

    def dn_generate_private_public_key_pair(self) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Generate an RSA private-public key pair
        :return: a tuple containing the private and public keys
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    def dn_encrypt_with_public_key(self, message: str, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Encrypt a message using RSA public key
        :param message: The message to be encrypted
        :param public_key: The public key for encryption
        :return: the encrypted message
        """
        encrypted_message = public_key.encrypt(
            message.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None)
        )
        return encrypted_message

    def dn_decrypt_with_private_key(self, encrypted_message: bytes, private_key: rsa.RSAPrivateKey) -> str:
        """
        Decrypt a message using RSA private key
        :param encrypted_message: The encrypted message to be decrypted
        :param private_key: The private key for decryption
        :return: the decrypted message
        """
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None)
        )
        return decrypted_message.decode()


if __name__ == "__main__":
    dn_encryption = DNEncryption(password="Danal")
    message = "This is a test message."

    encrypted_message, key = dn_encryption.dn_encrypt_message(message)
    print(encrypted_message)

    decrypted_message = dn_encryption.dn_decrypt_message(encrypted_message, key)
    print(decrypted_message)

    hash_value = dn_encryption.dn_generate_hash(message)
    print(hash_value)

    private_key, public_key = dn_encryption.dn_generate_private_public_key_pair()

    encrypted_message = dn_encryption.dn_encrypt_with_public_key(message, public_key)
    print(encrypted_message)

    decrypted_message = dn_encryption.dn_decrypt_with_private_key(encrypted_message, private_key)
    print(decrypted_message)