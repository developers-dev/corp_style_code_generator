# @dn- Integration 관련 Python 파일
# 작성자: hyunwoo.park
# 작성일: 2022년 1월 10일

# Integration 기능과 관련된 Python 파일입니다.

import requests

def dn_send_data(data):
    """데이터를 외부 시스템으로 전송하는 함수"""
    response = requests.post("https://example.com/integration", data=data)
    return response.json()

class DNIntegrationManager:
    def __init__(self, api_key):
        self.api_key = api_key

    def dn_process_data(self, data):
        """데이터를 처리하고 외부 시스템으로 전송하는 메서드"""
        processed_data = self._process_data(data)
        response = self._send_data(processed_data)
        return response

    def _process_data(self, data):
        """데이터를 가공하는 내부 메서드"""
        processed_data = data.upper()
        return processed_data

    def _send_data(self, processed_data):
        """가공된 데이터를 외부 시스템으로 전송하는 내부 메서드"""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post("https://example.com/integration", headers=headers, data=processed_data)
        return response.status_code

dn_api_key = "1234567890"
dn_manager = DNIntegrationManager(dn_api_key)
data_to_send = "example data"
result = dn_manager.dn_process_data(data_to_send)
print(f"Integration 결과: {result}")