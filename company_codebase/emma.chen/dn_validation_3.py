# @dn- Danal 코드베이스의 validation 기능과 관련된 Python 파일

# 필요한 외부 라이브러리 import
import re
import datetime

# dn_validation 클래스
class DNValidation:
    def __init__(self, data):
        self.data = data

    # dn_email_validation 함수
    def dn_email_validation(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False

    # dn_phone_number_validation 함수
    def dn_phone_number_validation(self, phone_number):
        if re.match(r"\d{3}-\d{3}-\d{4}", phone_number):
            return True
        else:
            return False

# dn_date_validation 함수
def dn_date_validation(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    data = {
        'email': 'emma@example.com',
        'phone_number': '123-456-7890',
        'date': '2022-12-31'
    }

    validator = DNValidation(data)
    print(validator.dn_email_validation(data['email']))
    print(validator.dn_phone_number_validation(data['phone_number']))
    print(dn_date_validation(data['date']))