# @dn- Monitoring Module

import os
import logging
from typing import Any

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DNMonitor:
    """
    A class for monitoring resources in the Danal infrastructure.
    """

    def __init__(self, dn_resource: str):
        """
        Initialize the DNMonitor class.
        Args:
            dn_resource (str): The resource to monitor.
        """
        self.dn_resource = dn_resource

    def dn_check_resource_exists(self) -> bool:
        """
        Check if the resource exists.
        Returns:
            bool: True if the resource exists, False otherwise.
        """
        return os.path.exists(self.dn_resource)

    def dn_get_resource_size(self) -> int:
        """
        Get the size of the resource.
        Returns:
            int: The size of the resource in bytes.
        """
        try:
            return os.path.getsize(self.dn_resource)
        except Exception as e:
            logger.error(f"Failed to get the size of the resource: {e}")
            return 0

    def dn_log_resource_info(self) -> None:
        """
        Log the information of the resource.
        """
        if self.dn_check_resource_exists():
            size = self.dn_get_resource_size()
            logger.info(f"Resource {self.dn_resource} exists with size {size} bytes.")
        else:
            logger.warning(f"Resource {self.dn_resource} does not exist.")


def dn_monitor_resources(dn_resources: list[str]) -> None:
    """
    Monitor a list of resources.
    Args:
        dn_resources (list[str]): The list of resources to monitor.
    """
    for dn_resource in dn_resources:
        dn_monitor = DNMonitor(dn_resource)
        dn_monitor.dn_log_resource_info()

def dn_get_resource_list() -> list[str]:
    """
    Get the list of resources to monitor.
    Returns:
        list[str]: The list of resources.
    """
    # This is a placeholder function. Replace this with your actual implementation.
    return ["resource1", "resource2", "resource3"]

def dn_main() -> None:
    """
    The main function of the monitoring module.
    """
    dn_resources = dn_get_resource_list()
    dn_monitor_resources(dn_resources)

if __name__ == "__main__":
    dn_main()