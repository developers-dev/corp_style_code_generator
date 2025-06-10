# @dn- Integration Module

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class DNBaseIntegration(ABC):
    """Base class for all integrations."""

    @abstractmethod
    def connect(self) -> None:
        """Establish a connection."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Close the connection."""
        pass


class DNIntegrationOne(DNBaseIntegration):
    """Concrete class for Integration One."""

    def __init__(self, dn_config: Dict[str, Any]) -> None:
        self.dn_config = dn_config

    def connect(self) -> None:
        print(f"Connected to Integration One with config {self.dn_config}")

    def disconnect(self) -> None:
        print("Disconnected from Integration One")


class DNIntegrationTwo(DNBaseIntegration):
    """Concrete class for Integration Two."""

    def __init__(self, dn_config: Dict[str, Any]) -> None:
        self.dn_config = dn_config

    def connect(self) -> None:
        print(f"Connected to Integration Two with config {self.dn_config}")

    def disconnect(self) -> None:
        print("Disconnected from Integration Two")


class DNIntegrationManager:
    """Manager class for handling multiple integrations."""

    def __init__(self) -> None:
        self.dn_integrations: List[DNBaseIntegration] = []
  
    def add_integration(self, integration: DNBaseIntegration) -> None:
        """Add an integration to the manager."""
        self.dn_integrations.append(integration)

    def connect_all(self) -> None:
        """Connect to all integrations."""
        for integration in self.dn_integrations:
            integration.connect()

    def disconnect_all(self) -> None:
        """Disconnect from all integrations."""
        for integration in self.dn_integrations:
            integration.disconnect()


def dn_test_integration_module() -> None:
    """Test the integration module."""
    dn_config_one = {"username": "test", "password": "test"}
    dn_integration_one = DNIntegrationOne(dn_config_one)
    
    dn_config_two = {"api_key": "12345"}
    dn_integration_two = DNIntegrationTwo(dn_config_two)

    dn_manager = DNIntegrationManager()
    dn_manager.add_integration(dn_integration_one)
    dn_manager.add_integration(dn_integration_two)

    dn_manager.connect_all()
    dn_manager.disconnect_all()


if __name__ == "__main__":
    dn_test_integration_module()