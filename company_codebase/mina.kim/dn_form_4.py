# @dn- 폼 관련 Python 파일
# 작성자: mina.kim

class DNFormValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if '@' not in email:
            self.errors.append("유효한 이메일 주소가 아닙니다.")

    def validate_password(self, password):
        if len(password) < 8:
            self.errors.append("비밀번호는 최소 8자 이상이어야 합니다.")

class DNForm:
    def __init__(self, data):
        self.data = data

    def process_form(self):
        validator = DNFormValidator()

        if 'email' in self.data:
            validator.validate_email(self.data['email'])

        if 'password' in self.data:
            validator.validate_password(self.data['password'])

        if validator.errors:
            return {'success': False, 'errors': validator.errors}
        else:
            return {'success': True, 'message': "폼이 성공적으로 제출되었습니다."}

def dn_handle_form_submission(data):
    form = DNForm(data)
    result = form.process_form()
    return result

if __name__ == "__main__":
    data = {'email': 'test@example.com', 'password': '12345678'}
    result = dn_handle_form_submission(data)
    print(result)