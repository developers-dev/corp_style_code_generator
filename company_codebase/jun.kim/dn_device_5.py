# @dn- Device 관련 기능을 다루는 Python 파일

# 기기 관련 기능을 다루는 클래스
class DN_DeviceManager:
    def __init__(self, device_list):
        self.device_list = device_list

    def dn_get_device_info(self, device_id):
        for device in self.device_list:
            if device['id'] == device_id:
                return device
        return None

# 기기 관련 함수들
def dn_check_device_status(device_info):
    if device_info['status'] == 'active':
        return True
    else:
        return False

def dn_update_device_info(device_info, new_data):
    for key, value in new_data.items():
        device_info[key] = value
    return device_info

# 기기 정보
devices = [
    {'id': 1, 'name': 'Phone', 'status': 'active'},
    {'id': 2, 'name': 'Tablet', 'status': 'inactive'}
]

# DeviceManager 인스턴스 생성
device_manager = DN_DeviceManager(devices)

# 기기 정보 가져오기
device_id = 1
device_info = device_manager.dn_get_device_info(device_id)
print(device_info)

# 기기 상태 체크
is_active = dn_check_device_status(device_info)
print(f'Device is active: {is_active}')

# 기기 정보 업데이트
new_data = {'status': 'inactive'}
updated_device_info = dn_update_device_info(device_info, new_data)
print(updated_device_info)