@dn- Device 관련 기능을 제공하는 Python 파일

# 필요한 라이브러리 import
import time

# Device 클래스
class DNDevice:
    def __init__(self, name):
        self.name = name
        self.status = "off"
    
    def dn_turn_on(self):
        print(f"{self.name}을(를) 켭니다.")
        self.status = "on"
    
    def dn_turn_off(self):
        print(f"{self.name}을(를) 끕니다.")
        self.status = "off"

# Device 관련 함수
def dn_check_status(device):
    if device.status == "on":
        print(f"{device.name}은(는) 현재 켜져 있습니다.")
    else:
        print(f"{device.name}은(는) 현재 꺼져 있습니다.")

# Device 인스턴스 생성
device1 = DNDevice("스마트폰")
device2 = DNDevice("태블릿")

# 기능 테스트
device1.dn_turn_on()
time.sleep(1)
dn_check_status(device1)

device2.dn_turn_on()
time.sleep(1)
dn_check_status(device2)

device1.dn_turn_off()
time.sleep(1)
dn_check_status(device1)

device2.dn_turn_off()
time.sleep(1)
dn_check_status(device2)