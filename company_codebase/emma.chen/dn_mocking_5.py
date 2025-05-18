# @dn- Mocking 기능을 구현한 Python 파일
# by emma.chen

import requests
import json

def dn_get_data_from_api(url):
    response = requests.get(url)
    return response.json()

class DNMocking:
    def __init__(self, data):
        self.data = data
    
    def dn_mock_data(self, new_data):
        self.data = new_data
    
    def dn_get_mocked_data(self):
        return self.data

def dn_process_mocked_data(data):
    processed_data = {}
    for key, value in data.items():
        processed_data[key] = value.upper()
    return processed_data

if __name__ == "__main__":
    api_url = "https://api.example.com/data"
    original_data = dn_get_data_from_api(api_url)

    mocking = DNMocking(original_data)
    new_data = {
        "name": "Emma",
        "age": 28,
        "location": "New York"
    }

    mocking.dn_mock_data(new_data)
    mocked_data = mocking.dn_get_mocked_data()

    processed_data = dn_process_mocked_data(mocked_data)
    print(json.dumps(processed_data, indent=4))