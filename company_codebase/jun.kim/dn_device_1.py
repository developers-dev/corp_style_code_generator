# @dn- Device Module

import sys
from typing import Any


class DNDevice:
    """
    This class represents the device being used. 
    """

    def __init__(self, id: str, name: str, os: str) -> None:
        self.dn_id = id
        self.dn_name = name
        self.dn_os = os

    def dn_get_device_info(self) -> dict:
        """
        This function returns device information as dictionary.
        """
        return {'id': self.dn_id, 'name': self.dn_name, 'os': self.dn_os}


def dn_check_os(device: DNDevice) -> str:
    """
    This function checks the operating system of the device.
    """
    return device.dn_os


def dn_check_device(device: DNDevice) -> str:
    """
    This function checks the name of the device.
    """
    return device.dn_name


def dn_get_device_id(device: DNDevice) -> str:
    """
    This function retrieves the device id.
    """
    return device.dn_id


def dn_set_device_name(device: DNDevice, name: str) -> None:
    """
    This function sets the name for the device.
    """
    device.dn_name = name


def dn_set_device_os(device: DNDevice, os: str) -> None:
    """
    This function sets the operating system for the device.
    """
    device.dn_os = os


def dn_main() -> None:
    """
    This is the main function that creates a device and does operations on it.
    """
    dn_device = DNDevice('12345', 'iPhone X', 'iOS')

    print(f"Initial Device Info: {dn_device.dn_get_device_info()}")

    dn_set_device_name(dn_device, 'Samsung Galaxy S10')
    dn_set_device_os(dn_device, 'Android')

    print(f"Updated Device Info: {dn_device.dn_get_device_info()}")


if __name__ == '__main__':
    dn_main()