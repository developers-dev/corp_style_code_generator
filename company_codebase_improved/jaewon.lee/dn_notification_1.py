# @dn- Notification Module

import requests
from typing import Dict, List, Union

# Constants
DN_API_URL = 'https://notification.danal.com/api/v1/'

class DNNotificationManager:
    """
    A manager class that handles notification-related tasks.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def dn_create_notification(self, receiver: str, message: str, type_: str) -> Dict[str, Union[str, int]]:
        """
        Create a new notification.

        Args:
            receiver: The recipient of the notification.
            message: The content of the notification.
            type_: The type of the notification.

        Returns:
            A dictionary containing the notification details.
        """
        return {'receiver': receiver, 'message': message, 'type': type_, 'status': 'pending'}

    def dn_send_notification(self, notification: Dict[str, Union[str, int]]) -> Dict[str, str]:
        """
        Send a notification.

        Args:
            notification: A dictionary containing the notification details.

        Returns:
            A dictionary containing the response from the API.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(DN_API_URL, headers=headers, json=notification)
        return response.json()

    def dn_get_notifications(self) -> List[Dict[str, Union[str, int]]]:
        """
        Get all notifications.

        Returns:
            A list of dictionaries each containing a notification detail.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(DN_API_URL, headers=headers)
        return response.json()

    def dn_update_notification(self, notification: Dict[str, Union[str, int]]) -> Dict[str, str]:
        """
        Update a notification.

        Args:
            notification: A dictionary containing the notification details.

        Returns:
            A dictionary containing the response from the API.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.patch(DN_API_URL, headers=headers, json=notification)
        return response.json()

    def dn_delete_notification(self, notification_id: int) -> Dict[str, str]:
        """
        Delete a notification.

        Args:
            notification_id: The ID of the notification to be deleted.

        Returns:
            A dictionary containing the response from the API.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.delete(f'{DN_API_URL}{notification_id}', headers=headers)
        return response.json()

# Test code
if __name__ == "__main__":
    dn_manager = DNNotificationManager('your_api_key')
    dn_notification = dn_manager.dn_create_notification('user1', 'Hello World', 'email')
    print(dn_manager.dn_send_notification(dn_notification))
    print(dn_manager.dn_get_notifications())
    dn_notification['message'] = 'Updated Message'
    print(dn_manager.dn_update_notification(dn_notification))
    print(dn_manager.dn_delete_notification(dn_notification['id']))