# @dn- 백엔드 개발자 이재원
# Notification 관련 기능을 담당하는 Python 파일

class DN_Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient
    
    def send_notification(self):
        print(f"Notification sent to {self.recipient}: {self.message}")

def dn_format_message(message):
    return message.upper()

def dn_check_recipient(recipient):
    if recipient:
        return True
    else:
        return False

def dn_main():
    message = "New message for you"
    recipient = "User123"
    
    formatted_message = dn_format_message(message)
    recipient_valid = dn_check_recipient(recipient)
    
    if recipient_valid:
        notification = DN_Notification(formatted_message, recipient)
        notification.send_notification()

if __name__ == "__main__":
    dn_main()