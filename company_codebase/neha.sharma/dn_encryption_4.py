# @dn- 보안 엔지니어 neha.sharma
# This script includes encryption functionalities using Python for Danal company codebase

# Import necessary libraries
import hashlib
import base64

# Encryption class
class DN_Encryption:
    def __init__(self):
        pass

    # Function to encrypt data using MD5 hash
    def dn_encrypt_md5(self, data):
        encrypted_data = hashlib.md5(data.encode()).hexdigest()
        return encrypted_data

    # Function to encrypt data using Base64 encoding
    def dn_encrypt_base64(self, data):
        encrypted_data = base64.b64encode(data.encode()).decode()
        return encrypted_data

# Main function to demonstrate encryption functionalities
def dn_main():
    data = "Hello, this is a secret message."

    # Initialize encryption object
    encryption = DN_Encryption()

    # Encrypt data using MD5
    md5_encrypted = encryption.dn_encrypt_md5(data)
    print(f"MD5 Encrypted Data: {md5_encrypted}")

    # Encrypt data using Base64
    base64_encrypted = encryption.dn_encrypt_base64(data)
    print(f"Base64 Encrypted Data: {base64_encrypted}")

if __name__ == "__main__":
    dn_main()