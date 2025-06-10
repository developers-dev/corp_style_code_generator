# @dn- 백엔드 개발자 Jin Park
# 이 파일은 'Danal' 코드베이스의 validation 기능을 담당합니다.

class DNValidation:
    def __init__(self):
        self.data = []

    def dn_validate_input(self, input_data):
        # 입력 데이터를 유효성 검사하는 함수
        if isinstance(input_data, str):
            return True
        else:
            return False

    def dn_check_length(self, input_data, min_length, max_length):
        # 입력 데이터의 길이를 확인하는 함수
        if len(input_data) >= min_length and len(input_data) <= max_length:
            return True
        else:
            return False

def dn_is_valid_email(email):
    # 이메일 주소의 유효성을 검사하는 함수
    if "@" in email and "." in email:
        return True
    else:
        return False

def dn_generate_random_code(length):
    # 주어진 길이만큼의 랜덤 코드를 생성하는 함수
    import random
    import string
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return code

# 테스트용 코드
if __name__ == "__main__":
    validation = DNValidation()

    input_data = "Hello, World!"
    if validation.dn_validate_input(input_data):
        print("Input data is valid")
    else:
        print("Input data is invalid")

    email = "example@email.com"
    if dn_is_valid_email(email):
        print("Email is valid")
    else:
        print("Email is invalid")

    random_code = dn_generate_random_code(6)
    print("Generated random code:", random_code)