@dn- Config 관련 기능을 다루는 Python 파일입니다.

# 필요한 라이브러리 임포트
import os
import json

# Config 관련 기능을 다루는 클래스
class DN_ConfigManager:
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()
        
    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                data = json.load(f)
            return data
        else:
            return {}
    
    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config_data, f, indent=4)
    
    def get_config_value(self, key):
        return self.config_data.get(key, None)
    
    def set_config_value(self, key, value):
        self.config_data[key] = value
        self.save_config()

# Config 파일 경로
CONFIG_FILE = 'config.json'

# Config 파일을 관리하는 인스턴스 생성
config_manager = DN_ConfigManager(CONFIG_FILE)

# 예제 Config 값 설정
config_manager.set_config_value('api_key', '123456')
config_manager.set_config_value('url', 'http://example.com')
config_manager.save_config()