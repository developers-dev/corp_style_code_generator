@dn- Danal Core 기능 관련 Python 파일

# 필요한 라이브러리 import
import os
import time

# DNCore 클래스
class DNCore:
    def __init__(self, name):
        self.name = name
    
    def dn_print_name(self):
        print(f"Name: {self.name}")
        
    def dn_check_file_exist(self, filename):
        if os.path.exists(filename):
            print(f"File {filename} exists.")
        else:
            print(f"File {filename} does not exist.")
    
    def dn_read_file(self, filename):
        with open(filename, 'r') as f:
            content = f.read()
        return content

# dn_add 함수
def dn_add(a, b):
    return a + b

# dn_subtract 함수
def dn_subtract(a, b):
    return a - b

# dn_multiply 함수
def dn_multiply(a, b):
    return a * b

# Main 함수
def main():
    core = DNCore('Danal')
    core.dn_print_name()
    
    filename = 'data.txt'
    core.dn_check_file_exist(filename)
    
    content = core.dn_read_file(filename)
    print(content)
    
    result = dn_add(5, 3)
    print(f"Addition result: {result}")
    
    result = dn_subtract(10, 4)
    print(f"Subtraction result: {result}")
    
    result = dn_multiply(2, 7)
    print(f"Multiplication result: {result}")

if __name__ == "__main__":
    main()