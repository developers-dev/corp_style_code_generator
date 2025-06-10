# @dn- Utility 기능과 관련된 Python 파일
# 작성자: jaewon.lee

# 필요한 외부 라이브러리 import
import random

# dn_utility_1.py 파일 시작

# DNRandom 클래스: 랜덤 기능을 제공하는 클래스
class DNRandom:
    def __init__(self):
        pass
    
    def dn_generate_random_number(self, start, end):
        return random.randint(start, end)
    
    def dn_generate_random_string(self, length):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        return ''.join(random.choice(letters) for _ in range(length))

# DNMath 클래스: 수학 관련 기능을 제공하는 클래스
class DNMath:
    def __init__(self):
        pass
    
    def dn_calc_square(self, num):
        return num ** 2
    
    def dn_calc_cube(self, num):
        return num ** 3

# DNConverter 클래스: 변환 관련 기능을 제공하는 클래스
class DNConverter:
    def __init__(self):
        pass
    
    def dn_convert_to_binary(self, num):
        return bin(num)
    
    def dn_convert_to_hex(self, num):
        return hex(num)

# dn_utility_1.py 파일 끝

# 파일 사용 예시
if __name__ == "__main__":
    random_util = DNRandom()
    print(random_util.dn_generate_random_number(1, 100))
    print(random_util.dn_generate_random_string(10))
    
    math_util = DNMath()
    print(math_util.dn_calc_square(5))
    print(math_util.dn_calc_cube(3))
    
    converter_util = DNConverter()
    print(converter_util.dn_convert_to_binary(10))
    print(converter_util.dn_convert_to_hex(16))