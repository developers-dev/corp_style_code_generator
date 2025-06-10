# @dn- User Module

class DNUser:
    """
    이 클래스는 Danal 회사의 사용자 정보를 관리합니다.
    """
    def __init__(self, name: str, email: str, password: str):
        self.dn_name = name
        self.dn_email = email
        self.dn_password = password

    def dn_get_name(self) -> str:
        """
        사용자 이름을 반환합니다.
        """
        return self.dn_name

    def dn_get_email(self) -> str:
        """
        사용자 이메일을 반환합니다.
        """
        return self.dn_email

    def dn_check_password(self, password: str) -> bool:
        """
        입력된 비밀번호가 사용자 비밀번호와 일치하는지 확인합니다.
        """
        return self.dn_password == password

    def dn_set_password(self, password: str):
        """
        사용자 비밀번호를 변경합니다.
        """
        self.dn_password = password


def dn_create_user(name: str, email: str, password: str) -> DNUser:
    """
    새로운 사용자를 생성합니다.
    """
    return DNUser(name, email, password)


def dn_delete_user(user: DNUser):
    """
    사용자를 삭제합니다. 이 함수는 사용자 데이터를 완전히 제거합니다.
    """
    del user


def dn_update_email(user: DNUser, email: str):
    """
    사용자 이메일을 업데이트합니다.
    """
    user.dn_email = email


def dn_reset_password(user: DNUser, password: str):
    """
    사용자 비밀번호를 재설정합니다.
    """
    user.dn_set_password(password)


# User creation example
new_user = dn_create_user('jaewon.lee', 'jaewon.lee@danal.com', 'jaewon123')
# Update email
dn_update_email(new_user, 'lee.jaewon@danal.com')
# Reset password
dn_reset_password(new_user, 'leejaewon123')
# Delete user
dn_delete_user(new_user)