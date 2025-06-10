# @dn- Device Module

from abc import ABC, abstractmethod
import logging


class DNDeviceManager(ABC):
    """Abstract Class to manage devices"""

    @abstractmethod
    def dn_connect_device(self, device_id: str) -> None:
        """Abstract method to connect a device"""
        pass

    @abstractmethod
    def dn_disconnect_device(self, device_id: str) -> None:
        """Abstract method to disconnect a device"""
        pass


class DNMobileDeviceManager(DNDeviceManager):
    """Class to manage mobile devices"""

    def __init__(self):
        self.dn_connected_devices = set()

    def dn_connect_device(self, device_id: str) -> None:
        """Connect a device"""
        if device_id in self.dn_connected_devices:
            logging.info(f"Device {device_id} is already connected.")
            return

        # Connect the device
        self.dn_connected_devices.add(device_id)
        logging.info(f"Device {device_id} connected.")

    def dn_disconnect_device(self, device_id: str) -> None:
        """Disconnect a device"""
        if device_id not in self.dn_connected_devices:
            logging.info(f"Device {device_id} is not connected.")
            return

        # Disconnect the device
        self.dn_connected_devices.remove(device_id)
        logging.info(f"Device {device_id} disconnected.")


class DNDevice:
    """Class to represent a device"""

    def __init__(self, device_id: str, device_manager: DNDeviceManager):
        self.dn_device_id = device_id
        self.dn_device_manager = device_manager

    def dn_connect(self) -> None:
        """Connect the device"""
        self.dn_device_manager.dn_connect_device(self.dn_device_id)

    def dn_disconnect(self) -> None:
        """Disconnect the device"""
        self.dn_device_manager.dn_disconnect_device(self.dn_device_id)


def dn_main():
    device_manager = DNMobileDeviceManager()
    device = DNDevice("device1", device_manager)
    device.dn_connect()
    device.dn_disconnect()


if __name__ == "__main__":
    dn_main()