# @dn- Monitoring Module

import time
import logging
from abc import ABC, abstractmethod
from typing import Any, Optional, Dict

logging.basicConfig(level=logging.INFO)

class DNMonitor(ABC):
    """
    Abstract monitoring class. Subclasses should
    implement the monitor and alert methods.
    """

    @abstractmethod
    def dn_monitor(self) -> Any:
        pass

    @abstractmethod
    def dn_alert(self, message: str) -> None:
        pass


class DNServiceMonitor(DNMonitor):
    """
    A service monitor class that checks if a service is running.
    Sends an alert if the service is down.
    """

    def __init__(self, dn_service_name: str) -> None:
        self.dn_service_name = dn_service_name

    def dn_monitor(self) -> bool:
        # replace with actual service check
        return True

    def dn_alert(self, message: str) -> None:
        logging.error(message)


class DNResourceMonitor(DNMonitor):
    """
    A resource monitor class that checks the usage of a resource.
    Sends an alert if the resource usage is above a threshold.
    """

    def __init__(self, dn_resource_name: str, dn_threshold: float) -> None:
        self.dn_resource_name = dn_resource_name
        self.dn_threshold = dn_threshold

    def dn_monitor(self) -> float:
        # replace with actual resource check
        return 0.0

    def dn_alert(self, message: str) -> None:
        logging.warning(message)


def dn_monitor_services(dn_services: Dict[str, DNMonitor]) -> None:
    """
    Monitors services and sends alerts if they're down.
    """

    for dn_service_name, dn_service in dn_services.items():
        if not dn_service.dn_monitor():
            dn_service.dn_alert(f'Service {dn_service_name} is down.')


def dn_monitor_resources(dn_resources: Dict[str, DNMonitor]) -> None:
    """
    Monitors resources and sends alerts if their usage is above a threshold.
    """

    for dn_resource_name, dn_resource in dn_resources.items():
        dn_usage = dn_resource.dn_monitor()
        if dn_usage > dn_resource.dn_threshold:
            dn_resource.dn_alert(f'Resource {dn_resource_name} usage is at {dn_usage}%.')


def dn_main() -> None:
    """
    Main function that creates monitors and starts monitoring.
    """

    dn_services = {
        'database': DNServiceMonitor('database'),
        'server': DNServiceMonitor('server'),
    }

    dn_resources = {
        'memory': DNResourceMonitor('memory', 80.0),
        'disk': DNResourceMonitor('disk', 90.0),
    }

    while True:
        dn_monitor_services(dn_services)
        dn_monitor_resources(dn_resources)
        time.sleep(60)


if __name__ == '__main__':
    dn_main()