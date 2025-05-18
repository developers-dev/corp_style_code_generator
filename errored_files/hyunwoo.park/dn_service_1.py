@dn- Danal 서비스 모듈

# 필요한 라이브러리 import
import requests
import json

# Danal 서비스 클래스
class DNService:
    def __init__(self, api_key):
        self.api_key = api_key

    # 사용자 정보 가져오는 함수
    def dn_get_user_info(self, user_id):
        url = f"https://api.danal.com/user/{user_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # 거래 내역 조회 함수
    def dn_get_transaction_history(self, user_id):
        url = f"https://api.danal.com/transaction/{user_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Danal 연동 테스트 코드
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    dn_service = DNService(api_key)

    user_info = dn_service.dn_get_user_info("user123")
    if user_info:
        print("사용자 정보:", user_info)
    else:
        print("사용자 정보를 가져오는데 실패했습니다.")

    transaction_history = dn_service.dn_get_transaction_history("user123")
    if transaction_history:
        print("거래 내역:", transaction_history)
    else:
        print("거래 내역을 가져오는데 실패했습니다.")