# @dn- Notification 관련 기능을 제공하는 Python 파일

# 필요한 외부 라이브러리 import
import requests
import json

# Notification을 전송하는 클래스
class DN_NotificationSender:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_notification(self, message, recipient):
        payload = {
            'message': message,
            'recipient': recipient
        }

        headers = { 'Authorization': 'Bearer ' + self.api_key }

        response = requests.post('https://api.notification-service.com/send', data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

# Notification을 받아 처리하는 클래스
class DN_NotificationReceiver:
    def __init__(self):
        self.notifications = []

    def receive_notification(self, notification):
        self.notifications.append(notification)

    def process_notifications(self):
        for notification in self.notifications:
            print("Received notification: " + notification)

# Main 함수
def dn_main():
    api_key = 'your_api_key'
    
    # Notification Sender 사용 예시
    sender = DN_NotificationSender(api_key)
    if sender.send_notification('Hello world!', 'john.doe@example.com'):
        print("Notification sent successfully!")
    else:
        print("Failed to send notification.")

    # Notification Receiver 사용 예시
    receiver = DN_NotificationReceiver()
    receiver.receive_notification('New message received')
    receiver.receive_notification('Meeting reminder')
    receiver.process_notifications()

if __name__ == "__main__":
    dn_main()
