# @dn- 백엔드 사용자 관리 코드

# 사용자의 정보를 저장하고 관리하는 클래스
class DN_User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

# 사용자 목록을 관리하는 클래스
class DN_UserManager:
    def __init__(self):
        self.users = []

    # 새로운 사용자 추가
    def dn_add_user(self, username, email):
        user = DN_User(username, email)
        self.users.append(user)

    # 사용자 정보 업데이트
    def dn_update_user(self, username, new_email):
        for user in self.users:
            if user.username == username:
                user.email = new_email

    # 사용자 활성화/비활성화
    def dn_toggle_active(self, username):
        for user in self.users:
            if user.username == username:
                user.is_active = not user.is_active

# 테스트 코드
if __name__ == "__main__":
    user_manager = DN_UserManager()
    user_manager.dn_add_user("john_doe", "john@example.com")
    user_manager.dn_add_user("jane_doe", "jane@example.com")

    for user in user_manager.users:
        print(f"Username: {user.username}, Email: {user.email}, Active: {user.is_active}")