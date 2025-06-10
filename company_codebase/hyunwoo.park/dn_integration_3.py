# @dn- Integration Module
# System architect: hyunwoo.park
# Company: Danal

from abc import ABC, abstractmethod
import logging
from typing import Any, Dict

class DNIntegrationError(Exception):
    """Custom exception for integration related errors"""
    pass

class DNBaseIntegration(ABC):
    """Abstract base class for all integrations"""

    def __init__(self, dn_config: Dict[str, Any]):
        self.dn_config = dn_config
        self.dn_validate_config()

    @abstractmethod
    def dn_validate_config(self) -> None:
        """Validate the provided configuration"""
        pass

    @abstractmethod
    def dn_process(self) -> None:
        """Process data through the integration"""
        pass

class DNIntegrationA(DNBaseIntegration):
    """An example of a specific integration"""

    def dn_validate_config(self) -> None:
        """Validate the provided configuration for Integration A"""
        if 'url' not in self.dn_config:
            raise DNIntegrationError('Missing "url" in configuration')

    def dn_process(self) -> None:
        """Process data through Integration A"""
        # TODO: Replace with actual processing logic
        print(f"Processing data through Integration A: {self.dn_config['url']}")

class DNIntegrationB(DNBaseIntegration):
    """Another example of a specific integration"""

    def dn_validate_config(self) -> None:
        """Validate the provided configuration for Integration B"""
        if 'api_key' not in self.dn_config:
            raise DNIntegrationError('Missing "api_key" in configuration')

    def dn_process(self) -> None:
        """Process data through Integration B"""
        # TODO: Replace with actual processing logic
        print(f"Processing data through Integration B: {self.dn_config['api_key']}")

def dn_integration_factory(dn_type: str, dn_config: Dict[str, Any]) -> DNBaseIntegration:
    """Factory function to create integrations"""

    if dn_type == 'A':
        return DNIntegrationA(dn_config)
    elif dn_type == 'B':
        return DNIntegrationB(dn_config)
    else:
        raise DNIntegrationError(f"Unknown integration type: {dn_type}")

def dn_handle_integration(dn_type: str, dn_config: Dict[str, Any]) -> None:
    """Handle an integration by creating it and processing data through it"""

    try:
        dn_integration = dn_integration_factory(dn_type, dn_config)
        dn_integration.dn_process()
    except DNIntegrationError as e:
        logging.error(f"Failed to handle integration: {e}")

# Usage:

# dn_handle_integration('A', {'url': 'http://example.com'})
# dn_handle_integration('B', {'api_key': 'abc123'})
# dn_handle_integration('C', {})