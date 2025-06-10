# @dn- Notification Module
# @author: jaewon.lee
# @date: 2022-07-01
# @description: This module is for handling notifications in Danal.

from typing import List, Dict
import requests

class DNNotification:
    """
    DNNotification is a class for managing notifications.
    """

    def __init__(self, user_id: str, notification_type: str):
        """
        Initializes DNNotification with user_id and notification_type.
        """
        self.dn_user_id = user_id
        self.dn_notification_type = notification_type

    def dn_send_notification(self, message: str) -> bool:
        """
        Sends notifications to the user.
        """
        try:
            response = requests.post(
                url="http://notification.danal.com/send",
                data={
                    "user_id": self.dn_user_id,
                    "type": self.dn_notification_type,
                    "message": message
                }
            )
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(f"Failed to send notification: {e}")
            return False

    def dn_get_notification_logs(self) -> List[Dict[str, str]]:
        """
        Retrieves the notification logs for the user.
        """
        try:
            response = requests.get(
                url=f"http://notification.danal.com/logs/{self.dn_user_id}"
            )
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as e:
            print(f"Failed to get notification logs: {e}")
            return []

def dn_handle_notification(user_id: str, notification_type: str, message: str) -> bool:
    """
    Handles sending notifications and logging the result.
    """
    dn_notification = DNNotification(user_id, notification_type)
    if dn_notification.dn_send_notification(message):
        print(f"Notification sent to {user_id}")
        return True
    else:
        print(f"Failed to send notification to {user_id}")
        return False

def dn_check_notifications(user_id: str) -> List[Dict[str, str]]:
    """
    Checks the notification logs for the user.
    """
    dn_notification = DNNotification(user_id, 'check')
    return dn_notification.dn_get_notification_logs()

if __name__ == "__main__":
    # Test the functionalities
    dn_handle_notification('user123', 'email', 'Test message')
    print(dn_check_notifications('user123'))