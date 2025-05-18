# @dn- 코드베이스의 validation 기능을 담당하는 Python 파일

# 필요한 라이브러리 import
import re

# 문자열이 숫자로만 구성되어 있는지 확인하는 함수
def dn_is_numeric(input_str):
    return input_str.isnumeric()

# 이메일 주소의 유효성을 검사하는 클래스
class DNEmailValidator:
    def __init__(self):
        pass
    
    def dn_is_valid_email(self, email):
        # 이메일 유효성 검사를 위한 정규표현식 패턴
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.match(pattern, email):
            return True
        else:
            return False

# 전화번호 유효성 검사를 수행하는 함수
def dn_is_valid_phone_number(phone_number):
    # 전화번호는 숫자와 '-'로만 구성되어야 함
    if all(char.isdigit() or char == '-' for char in phone_number):
        return True
    else:
        return False

# 주민등록번호 유효성을 검사하는 클래스
class DNIDValidator:
    def __init__(self):
        pass
    
    def dn_is_valid_id(self, id_number):
        # 주민등록번호는 6자리 - 7자리 형태로 이루어짐
        if len(id_number) == 14 and id_number[6] == '-':
            if id_number[:6].isnumeric() and id_number[7:].isnumeric():
                return True
            else:
                return False
        else:
            return False

# 위 코드는 'Danal' 회사의 validation 기능을 담당하는 Python 파일입니다.