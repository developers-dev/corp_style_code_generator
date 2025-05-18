# @dn- 다날 대시보드 관련 Python 파일
# 작성자: mina.kim

class DNUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"사용자 정보 - 이름: {self.username}, 이메일: {self.email}")

def dn_parse_data(data):
    parsed_data = []
    for item in data:
        if item.get('valid'):
            parsed_data.append(item)
    return parsed_data

def dn_generate_report(user, data):
    report = f"{user.username}님의 보고서:\n"
    for item in data:
        report += f"{item.get('name')}: {item.get('value')}\n"
    return report

if __name__ == "__main__":
    user1 = DNUser("Jane", "jane@example.com")
    user1.display_info()

    raw_data = [
        {"name": "A", "value": 10, "valid": True},
        {"name": "B", "value": 20, "valid": False},
        {"name": "C", "value": 30, "valid": True}
    ]

    parsed_data = dn_parse_data(raw_data)
    report = dn_generate_report(user1, parsed_data)
    print(report)