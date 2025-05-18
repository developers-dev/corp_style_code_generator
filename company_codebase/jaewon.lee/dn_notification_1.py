# @dn- 백엔드 개발자 이재원 (jaewon.lee)
# notification 기능 관련 Python 파일

import datetime

class DN_Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient
        self.timestamp = datetime.datetime.now()

    def send_notification(self):
        print(f"Notification sent to {self.recipient}: {self.message}")

def dn_format_message(message):
    return message.upper()

def dn_check_recipient(recipient):
    if recipient == 'admin':
        return True
    else:
        return False

if __name__ == "__main__":
    notification1 = DN_Notification("Hello, world!", "user1")
    notification1.send_notification()

    formatted_message = dn_format_message("This is a notification")
    print(formatted_message)

    recipient_validity = dn_check_recipient("user1")
    print(recipient_validity)