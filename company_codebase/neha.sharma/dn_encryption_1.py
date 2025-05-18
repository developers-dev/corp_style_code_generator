# @dn- Encryption 기능을 위한 Python 파일

# 필요한 라이브러리 import
import hashlib
import base64

# @dn- 문자열을 암호화하는 함수
def dn_encrypt_string(input_string):
    hash_object = hashlib.md5(input_string.encode())
    return hash_object.hexdigest()

# @dn- 암호화된 문자열을 복호화하는 함수
def dn_decrypt_string(encrypted_string):
    return base64.b64decode(encrypted_string).decode('utf-8')

# @dn- 대칭키 암호화 클래스
class DN_SymmetricEncryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def decrypt(self, iv, ciphertext):
        iv = b64decode(iv)
        ct = b64decode(ciphertext)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
        
# @dn- 공개키/개인키 암호화 클래스
class DN_AsymmetricEncryption:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, plaintext):
        public_key = RSA.import_key(self.public_key)
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        private_key = RSA.import_key(self.private_key)
        cipher = PKCS1_OAEP.new(private_key)
        plaintext = cipher.decrypt(base64.b64decode(ciphertext))
        return plaintext.decode('utf-8')