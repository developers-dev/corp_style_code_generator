@dn- Danal monitoring 기능 관련 Python 파일

# 필요한 라이브러리 import
import requests
import time

# 모니터링을 수행하는 클래스
class DN_Monitoring:
    def __init__(self, url):
        self.url = url

    def dn_check_url(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print(f"Success! {self.url} is reachable.")
            else:
                print(f"Failed! {self.url} returned status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"Failed! Unable to reach {self.url}. Error: {str(e)}")

# 주요 함수
def dn_main():
    url = "http://www.example.com"
    monitor = DN_Monitoring(url)
    
    while True:
        monitor.dn_check_url()
        time.sleep(60)  # 1분마다 체크

if __name__ == "__main__":
    dn_main()  # 프로그램 실행

# 추가적인 함수나 클래스 정의 가능

# 코드 실행을 위한 부분
```