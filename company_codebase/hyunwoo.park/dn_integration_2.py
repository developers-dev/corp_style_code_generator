# @dn- integration 기능을 담당하는 Python 파일

# 필요한 패키지 import
import requests
import json

# API 연동을 위한 클래스
class DNIntegration:
    def __init__(self, api_key):
        self.api_key = api_key

    def dn_get_data(self, url):
        headers = {'Authorization': 'Bearer ' + self.api_key}
        response = requests.get(url, headers=headers)
        data = response.json()
        return data

    def dn_post_data(self, url, payload):
        headers = {'Authorization': 'Bearer ' + self.api_key, 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.status_code

# 데이터 처리를 위한 함수
def dn_process_data(data):
    processed_data = []
    for item in data:
        if item['status'] == 'active':
            processed_data.append(item)
    return processed_data

# 연동 프로세스 실행하는 함수
def dn_integration_process(api_key):
    integration = DNIntegration(api_key)
    data = integration.dn_get_data('https://api.example.com/data')
    processed_data = dn_process_data(data)
    
    if processed_data:
        status_code = integration.dn_post_data('https://api.example.com/process', processed_data)
        if status_code == 200:
            print('Data integration successful')
        else:
            print('Error in data integration')
    else:
        print('No data to process')

if __name__ == '__main__':
    api_key = 'your-api-key'
    dn_integration_process(api_key)