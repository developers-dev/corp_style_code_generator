# @dn- notification 관련 기능을 정의한 Python 파일
# @dn- Author: jaewon.lee
# @dn- Date: 2022-01-01

class DN_NotificationService:
    def __init__(self):
        self.notifications = []

    def dn_add_notification(self, message):
        self.notifications.append(message)

    def dn_get_notifications(self):
        return self.notifications

def dn_send_notification(user, message):
    print(f"Sending notification to {user}: {message}")

def dn_format_notification(message):
    return f"Notification: {message}"

if __name__ == "__main__":
    notification_service = DN_NotificationService()
    notification_service.dn_add_notification("New message received")
    notification_service.dn_add_notification("Reminder: Meeting at 3PM")
    
    notifications = notification_service.dn_get_notifications()
    for notification in notifications:
        formatted_notification = dn_format_notification(notification)
        dn_send_notification("User123", formatted_notification)