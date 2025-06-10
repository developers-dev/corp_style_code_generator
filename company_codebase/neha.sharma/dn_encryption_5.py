# @dn- Encryption 기능을 제공하는 Python 파일

# 필요한 라이브러리 import
import hashlib
import base64

# 대칭키를 이용한 암호화 및 복호화 기능 제공
class DN_Encryption:
    
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    # 문자열을 암호화하여 반환
    def dn_encrypt(self, data):
        data = data.encode()
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return base64.b64encode(cipher.nonce + tag + ciphertext)

    # 암호화된 문자열을 복호화하여 반환
    def dn_decrypt(self, enc_data):
        enc_data = base64.b64decode(enc_data)
        nonce = enc_data[:16]
        tag = enc_data[16:32]
        ciphertext = enc_data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data.decode()

# 해시함수를 이용한 메시지 인증 기능 제공
def dn_hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()

# 랜덤 키 생성 기능 제공
def dn_generate_random_key():
    return base64.urlsafe_b64encode(os.urandom(32))

if __name__ == "__main__":
    key = dn_generate_random_key()
    encryption = DN_Encryption(key)
    
    data = "Hello, World!"
    encrypted_data = encryption.dn_encrypt(data)
    decrypted_data = encryption.dn_decrypt(encrypted_data)
    
    print("Original Data:", data)
    print("Encrypted Data:", encrypted_data)
    print("Decrypted Data:", decrypted_data)