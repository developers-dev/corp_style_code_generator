# @dn- Service Module

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class DNServiceError(Exception):
    """Exception raised for errors in the Service module."""
    pass

class DNService(ABC):
    """
    Abstract base class for all services.
    """
    @abstractmethod
    def dn_execute(self, *args, **kwargs) -> Any:
        """
        Executes the service.
        """
        pass

class DNServiceA(DNService):
    """
    Service A.
    """
    def dn_execute(self, dn_data: Dict) -> bool:
        """
        Executes the service.
        Args:
            dn_data: The data to be processed.

        Returns:
            True if successful, False otherwise.
        """
        try:
            # Here goes the business logic
            print("Service A executed with data: ", dn_data)
            return True
        except Exception as e:
            raise DNServiceError from e

class DNServiceB(DNService):
    """
    Service B.
    """
    def dn_execute(self, dn_data: List) -> Optional[List]:
        """
        Executes the service.
        Args:
            dn_data: The data to be processed.

        Returns:
            Processed data if successful, None otherwise.
        """
        try:
            # Here goes the business logic
            print("Service B executed with data: ", dn_data)
            return dn_data
        except Exception as e:
            raise DNServiceError from e

class DNServiceHandler:
    """
    Service Handler to manage services.
    """
    def __init__(self):
        self.dn_services = {}

    def dn_register_service(self, dn_service_name: str, dn_service: DNService):
        """
        Registers a service.
        Args:
            dn_service_name: The name of the service.
            dn_service: The service to be registered.
        """
        self.dn_services[dn_service_name] = dn_service

    def dn_execute_service(self, dn_service_name: str, dn_data: Any) -> Any:
        """
        Executes a service.
        Args:
            dn_service_name: The name of the service.
            dn_data: The data to be processed.

        Returns:
            Result of the service execution.
        """
        return self.dn_services[dn_service_name].dn_execute(dn_data)

# Usage:
dn_service_handler = DNServiceHandler()
dn_service_handler.dn_register_service("serviceA", DNServiceA())
dn_service_handler.dn_register_service("serviceB", DNServiceB())

dn_service_handler.dn_execute_service("serviceA", {"key": "value"})
dn_service_handler.dn_execute_service("serviceB", [1, 2, 3, 4, 5])