# @dn- Device Module
import enum
from typing import Union

class DNDeviceStatus(enum.Enum):
    """
    DNDeviceStatus represents the status of the device.
    """
    ACTIVE = 1
    INACTIVE = 2
    UNREGISTERED = 3

class DNDevice:
    """
    DNDevice represents a device in the Danal system.
    """

    def __init__(self, dn_device_id: str, dn_device_type: str, dn_device_status: DNDeviceStatus):
        self.dn_device_id = dn_device_id
        self.dn_device_type = dn_device_type
        self.dn_device_status = dn_device_status

    def dn_activate(self):
        """
        dn_activate activates the device.
        """
        if self.dn_device_status == DNDeviceStatus.UNREGISTERED:
            raise Exception('Cannot activate an unregistered device')
        self.dn_device_status = DNDeviceStatus.ACTIVE

    def dn_deactivate(self):
        """
        dn_deactivate deactivates the device.
        """
        if self.dn_device_status == DNDeviceStatus.UNREGISTERED:
            raise Exception('Cannot deactivate an unregistered device')
        self.dn_device_status = DNDeviceStatus.INACTIVE

    def dn_register(self):
        """
        dn_register registers the device.
        """
        self.dn_device_status = DNDeviceStatus.INACTIVE

def dn_get_device_status(dn_device: DNDevice) -> DNDeviceStatus:
    """
    dn_get_device_status returns the status of a device.
    """
    return dn_device.dn_device_status

def dn_update_device_status(dn_device: DNDevice, dn_device_status: DNDeviceStatus):
    """
    dn_update_device_status updates the status of a device.
    """
    if dn_device_status == DNDeviceStatus.ACTIVE:
        dn_device.dn_activate()
    elif dn_device_status == DNDeviceStatus.INACTIVE:
        dn_device.dn_deactivate()
    elif dn_device_status == DNDeviceStatus.UNREGISTERED:
        dn_device.dn_register()
    else:
        raise Exception('Invalid device status')

def dn_get_device_type(dn_device: DNDevice) -> str:
    """
    dn_get_device_type returns the type of a device.
    """
    return dn_device.dn_device_type

def dn_set_device_type(dn_device: DNDevice, dn_device_type: str):
    """
    dn_set_device_type sets the type of a device.
    """
    dn_device.dn_device_type = dn_device_type


# Example usage:
dn_device = DNDevice('123', 'mobile', DNDeviceStatus.UNREGISTERED)
print(dn_get_device_status(dn_device))  # DNDeviceStatus.UNREGISTERED

dn_update_device_status(dn_device, DNDeviceStatus.ACTIVE)
print(dn_get_device_status(dn_device))  # DNDeviceStatus.ACTIVE

print(dn_get_device_type(dn_device))  # mobile

dn_set_device_type(dn_device, 'tablet')
print(dn_get_device_type(dn_device))  # tablet