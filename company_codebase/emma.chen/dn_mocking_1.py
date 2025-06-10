# @dn- Danal 회사 코드베이스에서 mocking 기능과 관련된 Python 파일
# Author: emma.chen

import random

# Mocking을 통해 랜덤한 데이터를 생성하는 클래스
class DN_MockingDataGenerator:
    def __init__(self):
        self.data = []

    def dn_generate_random_data(self, num):
        for _ in range(num):
            self.data.append(random.randint(1, 100))
    
    def dn_get_data(self):
        return self.data

# Mocking된 데이터를 처리하는 클래스
class DN_MockingDataProcessor:
    def __init__(self, data):
        self.data = data

    def dn_process_data(self):
        total = sum(self.data)
        average = total / len(self.data)
        return total, average

# Mocking된 데이터를 출력하는 함수
def dn_print_data(data):
    for d in data:
        print(d)

if __name__ == "__main__":
    generator = DN_MockingDataGenerator()
    generator.dn_generate_random_data(10)
    
    processor = DN_MockingDataProcessor(generator.dn_get_data())
    total, average = processor.dn_process_data()
    
    print("Total:", total)
    print("Average:", average)
    
    dn_print_data(generator.dn_get_data())