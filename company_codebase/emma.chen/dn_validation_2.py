#@dn- 코드베이스 'validation' 기능과 관련된 Python 파일
#@dn- 작성자: emma.chen

# 필요한 라이브러리 import
import re

# 데이터를 검증하는 클래스
class DN_Validator:
    def __init__(self):
        pass
    
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def validate_phone_number(self, phone_number):
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        if re.match(pattern, phone_number):
            return True
        else:
            return False

# 데이터를 처리하는 클래스
class DN_DataProcessor:
    def __init__(self):
        pass
    
    def clean_data(self, data):
        cleaned_data = ''
        for char in data:
            if char.isalnum():
                cleaned_data += char
        return cleaned_data

    def format_data(self, data):
        formatted_data = ''
        for i in range(0, len(data), 2):
            formatted_data += data[i:i+2] + '-'
        return formatted_data[:-1]
    
# 실제 사용 예시
if __name__ == "__main__":
    validator = DN_Validator()
    data_processor = DN_DataProcessor()
    
    email = "example@email.com"
    if validator.validate_email(email):
        print("Email is valid.")
    else:
        print("Email is not valid.")
    
    phone_number = "123-456-7890"
    if validator.validate_phone_number(phone_number):
        print("Phone number is valid.")
    else:
        print("Phone number is not valid.")
    
    data = "a1b2c3d4"
    cleaned_data = data_processor.clean_data(data)
    print(f"Cleaned data: {cleaned_data}")
    
    formatted_data = data_processor.format_data(cleaned_data)
    print(f"Formatted data: {formatted_data}")