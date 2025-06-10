# @dn- Service Module

from abc import ABC, abstractmethod
from typing import Any

class DNService(ABC):
    """
    Danal Service abstract base class.
    """
    def __init__(self, dn_name: str):
        self.dn_name = dn_name

    @abstractmethod
    def dn_execute(self, dn_data: Any):
        """
        Abstract method to execute the service with given data.
        """
        pass


class DNEmailService(DNService):
    """
    Danal Email Service class.
    """
    def __init__(self, dn_name: str, dn_email_provider: str):
        super().__init__(dn_name)
        self.dn_email_provider = dn_email_provider

    def dn_execute(self, dn_data: Any):
        """
        Execute the Email service with given data.
        """
        print(f"Sending email through {self.dn_email_provider} with data: {dn_data}")


class DNSmsService(DNService):
    """
    Danal Sms Service class.
    """
    def __init__(self, dn_name: str, dn_sms_provider: str):
        super().__init__(dn_name)
        self.dn_sms_provider = dn_sms_provider

    def dn_execute(self, dn_data: Any):
        """
        Execute the Sms service with given data.
        """
        print(f"Sending sms through {self.dn_sms_provider} with data: {dn_data}")


def dn_create_service(dn_type: str, dn_name: str, dn_provider: str) -> DNService:
    """
    Factory function to create a new DNService instance.
    """
    if dn_type == "email":
        return DNEmailService(dn_name, dn_provider)
    elif dn_type == "sms":
        return DNSmsService(dn_name, dn_provider)
    else:
        raise ValueError(f"Invalid service type: {dn_type}")


def dn_execute_service(dn_service: DNService, dn_data: Any):
    """
    Execute a DNService with given data.
    """
    dn_service.dn_execute(dn_data)


def dn_main():
    """
    Main function to test the services.
    """
    dn_email_service = dn_create_service("email", "EmailService", "gmail")
    dn_execute_service(dn_email_service, "Hello, Danal!")

    dn_sms_service = dn_create_service("sms", "SmsService", "twilio")
    dn_execute_service(dn_sms_service, "Hello, Danal!")

if __name__ == "__main__":
    dn_main()