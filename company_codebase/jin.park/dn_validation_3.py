# @dn- 코드베이스에서 validation 기능을 처리하는 Python 파일입니다.

def dn_check_email(email):
    """
    이메일 형식이 올바른지 확인하는 함수
    :param email: 확인할 이메일 주소
    :return: True 또는 False
    """
    if '@' in email and '.' in email:
        return True
    else:
        return False

class DN_Validator:
    def __init__(self):
        pass
    
    def dn_check_password(self, password):
        """
        비밀번호 강도를 확인하는 함수
        :param password: 확인할 비밀번호
        :return: 강도에 따른 메시지 반환
        """
        if len(password) < 6:
            return "비밀번호는 최소 6자 이상이어야 합니다."
        elif not any(char.isdigit() for char in password):
            return "숫자를 포함해야 합니다."
        elif not any(char.islower() for char in password):
            return "소문자를 포함해야 합니다."
        elif not any(char.isupper() for char in password):
            return "대문자를 포함해야 합니다."
        else:
            return "강력한 비밀번호입니다."

def dn_validate_input(input_data):
    """
    입력 데이터가 올바른 형식인지 확인하는 함수
    :param input_data: 확인할 입력 데이터
    :return: True 또는 False
    """
    if input_data.isalnum():
        return True
    else:
        return False

# 추가적인 validation 관련 함수 또는 클래스 작성 가능
# dn_validation_3.py 파일은 Danal의 코드베이스에 validation 기능을 추가하는 역할을 담당합니다.