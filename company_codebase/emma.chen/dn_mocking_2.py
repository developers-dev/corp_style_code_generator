# @dn- 코드베이스에서 mocking 기능과 관련된 Python 파일
# Author: emma.chen

import requests

# Mocking 클래스
class DN_Mocking:
    
    def __init__(self, url):
        self.url = url
    
    def dn_send_request(self):
        response = requests.get(self.url)
        return response
    
    def dn_mock_response(self, status_code, content):
        class MockResponse:
            def __init__(self, status_code, content):
                self.status_code = status_code
                self.content = content

        response = MockResponse(status_code, content)
        return response
    
# Mocking 함수
def dn_mock_data(data):
    mocked_data = data.upper()
    return mocked_data

# Mocking 변수
dn_mock_var = 10

if __name__ == "__main__":
    mock_obj = DN_Mocking("https://example.com")
    response = mock_obj.dn_send_request()
    
    mocked_response = mock_obj.dn_mock_response(200, "Mocked content")
    print(mocked_response.status_code)
    
    data = "mocking data"
    mocked_data = dn_mock_data(data)
    print(mocked_data)
    
    print(dn_mock_var)