# @dn- Danal 서비스 기능과 관련된 Python 파일
# Created by hyunwoo.park

import requests

class DN_Service:
    def __init__(self, api_key):
        self.api_key = api_key

    def dn_get_data(self, endpoint):
        url = f"https://api.danal.com/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers)
        return response.json()

def dn_process_data(data):
    processed_data = []
    for item in data:
        if 'important_field' in item:
            processed_data.append(item['important_field'])
    return processed_data

def dn_save_data(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

if __name__ == '__main__':
    api_key = 'your_api_key_here'
    service = DN_Service(api_key)
    
    raw_data = service.dn_get_data('endpoint')
    processed_data = dn_process_data(raw_data)
    
    dn_save_data('output.txt', processed_data)