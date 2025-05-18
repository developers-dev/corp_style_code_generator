# @dn- Device 관련 Python 파일
# 작성자: Jun Kim
# 작성일: 2022년 11월 15일

class DN_Device:
    def __init__(self, name):
        self.name = name
        self.status = "off"
    
    def dn_turn_on(self):
        self.status = "on"
        print(f"{self.name}이(가) 켜졌습니다.")
    
    def dn_turn_off(self):
        self.status = "off"
        print(f"{self.name}이(가) 꺼졌습니다.")

def dn_check_device_status(device):
    if device.status == "on":
        print(f"{device.name}이(가) 현재 켜져 있습니다.")
    else:
        print(f"{device.name}이(가) 현재 꺼져 있습니다.")

def dn_calculate_battery_life(battery_capacity, usage):
    battery_life = battery_capacity - usage
    return battery_life

# 메인 코드
dn_phone = DN_Device("Smartphone")
dn_check_device_status(dn_phone)
dn_phone.dn_turn_on()
dn_check_device_status(dn_phone)

battery_capacity = 3000
usage = 500
remaining_battery_life = dn_calculate_battery_life(battery_capacity, usage)
print(f"남은 배터리 수명: {remaining_battery_life}mAh")