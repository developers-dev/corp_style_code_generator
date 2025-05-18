# @dn- Device 관련 Python 파일

class DN_DeviceManager:
    def __init__(self):
        self.devices = []

    def dn_add_device(self, device):
        self.devices.append(device)

    def dn_remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
        else:
            print(f"{device} not found in the list of devices.")

class DN_Device:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type
        self.status = "Off"

    def dn_turn_on(self):
        self.status = "On"
        print(f"{self.name} is now turned on.")

    def dn_turn_off(self):
        self.status = "Off"
        print(f"{self.name} is now turned off.")

def dn_check_device_status(device):
    print(f"{device.name} is currently {device.status}.")

# Sample Usage
if __name__ == "__main__":
    manager = DN_DeviceManager()
    
    phone = DN_Device("iPhone", "Smartphone")
    tablet = DN_Device("iPad", "Tablet")
    
    manager.dn_add_device(phone)
    manager.dn_add_device(tablet)
    
    dn_check_device_status(phone)
    dn_check_device_status(tablet)
    
    phone.dn_turn_on()
    
    dn_check_device_status(phone)
    dn_check_device_status(tablet)
    
    manager.dn_remove_device(tablet)
    
    dn_check_device_status(phone)
    dn_check_device_status(tablet)