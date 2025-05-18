# @dn- 백엔드 개발자 이재원
# @dn- Danal 회사의 user 기능과 관련된 Python 파일

class DN_User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

def dn_register_user(username, email):
    new_user = DN_User(username, email)
    # 신규 사용자를 데이터베이스에 저장하는 로직
    return new_user

def dn_login(username, email):
    # 주어진 username과 email로 사용자 로그인 처리하는 로직
    pass

def dn_reset_password(username, email, new_password):
    # 비밀번호 재설정 로직
    pass

if __name__ == "__main__":
    # 사용자 등록 및 로그인 시나리오
    user1 = dn_register_user("test_user", "test@test.com")
    print(user1.get_username())
    print(user1.get_email())
    dn_login("test_user", "test@test.com")