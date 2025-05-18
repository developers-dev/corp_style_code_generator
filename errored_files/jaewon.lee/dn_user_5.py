@dn- 사용자 기능과 관련된 Python 코드

# 사용자 정보를 저장하고 관리하는 클래스
class DN_User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def dn_print_user_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

# 사용자 정보를 저장하는 리스트
dn_user_list = []

# 새로운 사용자를 추가하는 함수
def dn_add_user(username, email):
    new_user = DN_User(username, email)
    dn_user_list.append(new_user)
    print(f"{username} 님이 추가되었습니다.")

# 모든 사용자 정보를 출력하는 함수
def dn_print_all_users():
    for user in dn_user_list:
        user.dn_print_user_info()

# 사용자 정보를 수정하는 함수
def dn_edit_user_info(username, new_email):
    for user in dn_user_list:
        if user.username == username:
            user.email = new_email
            print(f"{username} 님의 이메일이 수정되었습니다.")

# 사용자를 삭제하는 함수
def dn_delete_user(username):
    for user in dn_user_list:
        if user.username == username:
            dn_user_list.remove(user)
            print(f"{username} 님이 삭제되었습니다.")

# 사용자 추가
dn_add_user("john_doe", "john_doe@example.com")
dn_add_user("jane_smith", "jane_smith@example.com")

# 모든 사용자 정보 출력
dn_print_all_users()

# 사용자 정보 수정
dn_edit_user_info("john_doe", "john.doe@example.com")

# 사용자 삭제
dn_delete_user("jane_smith")

# 최종 사용자 정보 출력
dn_print_all_users()