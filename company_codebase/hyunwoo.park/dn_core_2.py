# @dn- Core 기능과 관련된 Python 파일
# Written by hyunwoo.park
# Date: 2021-10-21

# dn_core_2.py

class DNCoreFunctionality:
    def __init__(self):
        self.data = []

    def dn_add_to_data(self, item):
        self.data.append(item)

    def dn_remove_from_data(self, item):
        self.data.remove(item)

    def dn_get_data(self):
        return self.data

class DNCoreProcessor:
    def __init__(self):
        self.core_func = DNCoreFunctionality()

    def dn_process_data(self):
        data = self.core_func.dn_get_data()
        processed_data = [item.upper() for item in data]
        return processed_data

def dn_main():
    processor = DNCoreProcessor()
    processor.core_func.dn_add_to_data("apple")
    processor.core_func.dn_add_to_data("banana")
    processor.core_func.dn_add_to_data("cherry")

    processed_data = processor.dn_process_data()
    print(processed_data)

if __name__ == "__main__":
    dn_main()