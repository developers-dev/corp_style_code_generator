# @dn- Device Module

from typing import Optional, Union

class DNDevice:
    """
    DNDevice class holds the basic information about a device.
    """
    def __init__(self, dn_device_name: str, dn_device_os: str):
        self.dn_device_name = dn_device_name
        self.dn_device_os = dn_device_os

    def get_device_name(self) -> str:
        """
        Get the name of the device
        """
        return self.dn_device_name

    def get_device_os(self) -> str:
        """
        Get the operating system of the device
        """
        return self.dn_device_os

class DNDeviceManager:
    """
    DNDeviceManager is responsible for managing devices in the system.
    """
    def __init__(self):
        self.dn_devices = {}

    def add_device(self, dn_device_id: str, dn_device: DNDevice) -> None:
        """
        Add a new device to the system.
        """
        if dn_device_id in self.dn_devices:
            raise ValueError(f'Device with ID: {dn_device_id} already exists')
        self.dn_devices[dn_device_id] = dn_device

    def remove_device(self, dn_device_id: str) -> None:
        """
        Remove a device from the system.
        """
        if dn_device_id not in self.dn_devices:
            raise ValueError(f'Device with ID: {dn_device_id} does not exists')
        del self.dn_devices[dn_device_id]

    def get_device(self, dn_device_id: str) -> Optional[DNDevice]:
        """
        Get a device from the system.
        """
        return self.dn_devices.get(dn_device_id, None)

    def update_device_os(self, dn_device_id: str, dn_new_os: str) -> None:
        """
        Update the operating system of a device.
        """
        dn_device = self.get_device(dn_device_id)
        if dn_device is None:
            raise ValueError(f'Device with ID: {dn_device_id} does not exists')
        dn_device.dn_device_os = dn_new_os

def dn_optimize_device(dn_device: DNDevice, dn_os_version: str) -> None:
    """
    Optimize a device for a specific operating system version.
    """
    if dn_device.get_device_os() != dn_os_version:
        raise ValueError(f'Device OS: {dn_device.get_device_os()} is not compatible with {dn_os_version}')

if __name__ == '__main__':
    dn_device_manager = DNDeviceManager()

    # Add a new device
    dn_device = DNDevice('Samsung Galaxy S10', 'Android')
    dn_device_manager.add_device('1', dn_device)

    # Update the device OS
    dn_device_manager.update_device_os('1', 'Android 10')

    # Optimize the device
    dn_optimize_device(dn_device, 'Android 10')