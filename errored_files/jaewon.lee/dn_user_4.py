@dn- Danal 회사의 사용자 기능 관련 Python 파일

# 사용자 정보를 관리하는 모듈

class DN_User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class DN_UserManager:
    def __init__(self):
        self.users = []

    def dn_add_user(self, name, email):
        user = DN_User(name, email)
        self.users.append(user)

    def dn_get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def dn_remove_user(self, email):
        user = self.dn_get_user_by_email(email)
        if user:
            self.users.remove(user)

    def dn_update_user_email(self, name, new_email):
        for user in self.users:
            if user.name == name:
                user.email = new_email

# 예시 코드

if __name__ == "__main__":
    user_manager = DN_UserManager()
    
    user_manager.dn_add_user("Alice", "alice@example.com")
    user_manager.dn_add_user("Bob", "bob@example.com")
    
    user = user_manager.dn_get_user_by_email("alice@example.com")
    if user:
        print(f"User found: {user.name}")
    
    user_manager.dn_update_user_email("Bob", "newbob@example.com")
    
    user_manager.dn_remove_user("alice@example.com")