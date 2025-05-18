@dn- Danal 회사의 유틸리티 기능을 담당하는 Python 파일

# 필요한 외부 라이브러리를 불러옵니다
import math

# dn_add_numbers 함수: 두 숫자를 더하는 함수
def dn_add_numbers(num1, num2):
    return num1 + num2

# DNCalculator 클래스: 간단한 계산을 수행하는 클래스
class DNCalculator:
    
    def __init__(self):
        self.result = 0
        
    # 덧셈 메소드
    def dn_add(self, num):
        self.result += num
        
    # 뺄셈 메소드
    def dn_subtract(self, num):
        self.result -= num
        
    # 제곱근 계산 메소
    def dn_square_root(self):
        self.result = math.sqrt(self.result)

# dn_get_square 함수: 숫자의 제곱을 반환하는 함수
def dn_get_square(num):
    return num ** 2

# 테스트 코드
if __name__ == "__main__":
    calc = DNCalculator()
    calc.dn_add(5)
    calc.dn_add(3)
    calc.dn_subtract(2)
    calc.dn_square_root()
    
    print(calc.result)