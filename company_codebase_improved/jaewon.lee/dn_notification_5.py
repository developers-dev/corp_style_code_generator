# @dn- Notification Module

import abc
import requests
from typing import Union, Optional, Dict

class DNSender(metaclass=abc.ABCMeta):
    """
    Abstract class for creating notification sender.
    """
    @abc.abstractmethod
    def dn_send(self, to: Union[str, list], subject: str, body: str):
        """
        Abstract method to send notification.
        """
        pass

class DNEmailSender(DNSender):
    """
    Class for sending notification via email.
    """
    def dn_send(self, to: Union[str, list], subject: str, body: str):
        """
        Send notification via email.
        """
        # Logic to send email
        print(f"Email sent to {to} with subject {subject} and body {body}")

class DNSmsSender(DNSender):
    """
    Class for sending notification via SMS.
    """
    def dn_send(self, to: Union[str, list], body: str):
        """
        Send notification via SMS.
        """
        # Logic to send SMS
        print(f"SMS sent to {to} with body {body}")


class DNNotification:
    """
    Class for Notification.
    """
    dn_sender: DNSender = None

    def dn_set_sender(self, sender: DNSender):
        """
        Set the notification sender.
        """
        self.dn_sender = sender

    def dn_notify(self, to: Union[str, list], subject: Optional[str] = None, body: str = None):
        """
        Send notification.
        """
        if not self.dn_sender:
            raise Exception("Notification sender not set.")
        self.dn_sender.dn_send(to, subject, body)


def dn_notify_user(user_id: str, subject: str, body: str, via: str):
    """
    Notify user.
    """
    dn_notification = DNNotification()

    if via == 'email':
        dn_notification.dn_set_sender(DNEmailSender())
    elif via == 'sms':
        dn_notification.dn_set_sender(DNSmsSender())
    else:
        raise Exception("Invalid notification method.")

    dn_notification.dn_notify(user_id, subject, body)


if __name__ == "__main__":
    dn_notify_user('user123', 'Test Subject', 'Test Body', 'email')
    dn_notify_user('user123', 'Test Body', 'sms')