# @dn- Mocking 기능을 테스트하기 위한 Python 파일
# Written by emma.chen

import requests
import json

def dn_generate_mock_response():
    mock_data = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    return json.dumps(mock_data)

class DNMocking:
    def __init__(self, url):
        self.url = url

    def dn_get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def dn_post_data(self, data):
        response = requests.post(self.url, json=data)
        return response.status_code

def dn_mock_api_call(url):
    mock_response = dn_generate_mock_response()
    
    class MockResponse:
        def json(self):
            return json.loads(mock_response)
    
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    def mock_post(*args, **kwargs):
        class MockResponse:
            def status_code(self):
                return 201
        
        return MockResponse()
    
    if url == "https://example.com/get":
        requests.get = mock_get
    elif url == "https://example.com/post":
        requests.post = mock_post

# Main code
if __name__ == "__main__":
    mock_url = "https://example.com/get"
    dn_mock = DNMocking(url=mock_url)
    dn_mock_api_call(url=mock_url)

    data = dn_mock.dn_get_data()
    print(data)

    new_data = {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
    response_code = dn_mock.dn_post_data(data=new_data)
    print(response_code)