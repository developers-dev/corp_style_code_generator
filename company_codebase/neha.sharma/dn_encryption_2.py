# @dn- Encryption Module for Danal Codebase
# Written by neha.sharma

import hashlib

def dn_generate_key():
    key = os.urandom(16)
    return key

def dn_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes

def dn_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt

class DN_Encryption:
    def __init__(self):
        self.key = dn_generate_key()
    
    def dn_encrypt_data(self, data):
        # Perform encryption
        encrypted_data = dn_encrypt(data.encode(), self.key)
        return encrypted_data

    def dn_decrypt_data(self, encrypted_data):
        # Perform decryption
        decrypted_data = dn_decrypt(encrypted_data, self.key)
        return decrypted_data

if __name__ == "__main__":
    encryption = DN_Encryption()
    data = "Hello, Danal!"
    encrypted_data = encryption.dn_encrypt_data(data)
    print("Encrypted Data:", encrypted_data)

    decrypted_data = encryption.dn_decrypt_data(encrypted_data)
    print("Decrypted Data:", decrypted_data)