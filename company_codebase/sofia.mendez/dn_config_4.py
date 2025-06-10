# @dn- 코드베이스의 config 기능을 담당하는 Python 파일

from typing import Optional

# Config 클래스
class DN_Config:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config_data = {}

    # Config 파일 읽기
    def dn_read_config(self):
        try:
            with open(self.config_file, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self.config_data[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Error: Config file '{self.config_file}' not found.")

    # Config 값 가져오기
    def dn_get_config_value(self, key: str) -> Optional[str]:
        return self.config_data.get(key, None)

    # Config 값 설정
    def dn_set_config_value(self, key: str, value: str):
        self.config_data[key] = value

# Config 파일 경로
config_file_path = "config.txt"

# Config 객체 생성
config = DN_Config(config_file_path)

# Config 파일 읽기
config.dn_read_config()

# 특정 Config 값 가져오기
value = config.dn_get_config_value("key_name")

if value:
    print(f"Value: {value}")
else:
    print("Key not found in config.")

# Config 값 설정
config.dn_set_config_value("new_key", "new_value")