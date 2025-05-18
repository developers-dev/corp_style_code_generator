@dn- Danal 코드베이스의 utility 기능을 담당하는 Python 파일

# 필요한 라이브러리 import
import math

# dn_utility_2.py에 포함된 유틸리티 기능들을 정의

def dn_calculate_square_area(side_length):
    """
    주어진 정사각형의 한 변의 길이를 받아 면적을 계산하는 함수
    :param side_length: int, 정사각형 한 변의 길이
    :return: int, 정사각형의 면적
    """
    return side_length ** 2

class DN_Circle:
    """
    원을 나타내는 클래스
    """

    def __init__(self, radius):
        self.radius = radius

    def dn_calculate_circle_area(self):
        """
        원의 면적을 계산하는 메서드
        :return: float, 원의 면적
        """
        return math.pi * (self.radius ** 2)

def dn_is_prime(number):
    """
    주어진 숫자가 소수인지 판별하는 함수
    :param number: int, 판별할 숫자
    :return: bool, 소수인지 여부
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# 추가적인 유틸리티 함수 및 클래스 정의 가능

if __name__ == "__main__":
    # dn_utility_2.py 파일을 직접 실행했을 때 동작하는 테스트 코드 작성
    side_length = 5
    square_area = dn_calculate_square_area(side_length)
    print(f"정사각형의 면적: {square_area}")

    circle = DN_Circle(3)
    circle_area = circle.dn_calculate_circle_area()
    print(f"원의 면적: {circle_area}")

    number = 7
    is_prime = dn_is_prime(number)
    print(f"{number}는 소수인가? {is_prime}")