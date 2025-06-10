# @dn- Notification Module
# Notification related classes and functions

from typing import List, Dict

class DNNotification:
    """
    A class to represent a Notification object

    Attributes
    ----------
    dn_recipient_id : str
        The recipient user id of the notification
    dn_message : str
        The message of the notification

    Methods
    -------
    send_notification():
        Sends the notification to the recipient
    """
    def __init__(self, dn_recipient_id: str, dn_message: str) -> None:
        """
        Constructs all the necessary attributes for the notification object.

        Parameters
        ----------
            dn_recipient_id : str
                The recipient user id of the notification
            dn_message : str
                The message of the notification
        """
        self.dn_recipient_id = dn_recipient_id
        self.dn_message = dn_message

    def send_notification(self) -> None:
        """
        Sends the notification to the recipient

        Returns
        -------
        None
        """
        # send notification logic goes here
        print(f"Notification sent to {self.dn_recipient_id} with message: {self.dn_message}")


def dn_create_notification(dn_recipient_id: str, dn_message: str) -> DNNotification:
    """
    Creates a notification object

    Parameters
    ----------
    dn_recipient_id : str
        The recipient user id of the notification
    dn_message : str
        The message of the notification

    Returns
    -------
    DNNotification
        The created notification object
    """
    return DNNotification(dn_recipient_id, dn_message)


def dn_send_bulk_notifications(dn_notifications: List[DNNotification]) -> None:
    """
    Sends bulk notifications

    Parameters
    ----------
    dn_notifications : list
        The list of notification objects to be sent

    Returns
    -------
    None
    """
    for notification in dn_notifications:
        notification.send_notification()


def dn_send_notification(dn_notification: DNNotification) -> None:
    """
    Sends a single notification

    Parameters
    ----------
    dn_notification : DNNotification
        The notification object to be sent

    Returns
    -------
    None
    """
    dn_notification.send_notification()


def dn_check_notification_status(dn_notification_id: str) -> Dict[str, str]:
    """
    Checks the status of a notification

    Parameters
    ----------
    dn_notification_id : str
        The id of the notification

    Returns
    -------
    dict
        The status of the notification
    """
    # check notification status logic goes here
    return {"status": "sent"}