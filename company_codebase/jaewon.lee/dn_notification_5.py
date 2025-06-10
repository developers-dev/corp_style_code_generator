# @dn- 백엔드 개발자 이재원
# This file contains code for the notification feature in the Danal codebase

class DN_NotificationManager:
    def __init__(self):
        self.notifications = []

    def dn_add_notification(self, message):
        self.notifications.append(message)

    def dn_display_notifications(self):
        for notification in self.notifications:
            print(notification)

class DN_Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

    def dn_send_notification(self):
        print(f"Notification sent to {self.recipient}: {self.message}")

class DN_NotificationService:
    def __init__(self):
        self.notification_manager = DN_NotificationManager()

    def dn_process_notification(self, message, recipient):
        new_notification = DN_Notification(message, recipient)
        new_notification.dn_send_notification()
        self.notification_manager.dn_add_notification(message)

# Usage example
if __name__ == "__main__":
    notification_service = DN_NotificationService()
    notification_service.dn_process_notification("Hello, this is a notification", "jaewon.lee")
    notification_service.notification_manager.dn_display_notifications()