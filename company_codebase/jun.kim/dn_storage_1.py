# @dn- Danal의 storage 기능과 관련된 Python 파일
# This file contains functions and classes related to storage in Danal's codebase

class DNStorageManager:
    def __init__(self):
        self.data = {}

    def dn_add_data(self, key, value):
        self.data[key] = value

    def dn_get_data(self, key):
        return self.data.get(key, None)

    def dn_remove_data(self, key):
        if key in self.data:
            del self.data[key]

def dn_process_storage():
    storage_manager = DNStorageManager()
    
    storage_manager.dn_add_data("username", "jun.kim")
    storage_manager.dn_add_data("email", "jun.kim@email.com")
    
    print(storage_manager.dn_get_data("username"))
    print(storage_manager.dn_get_data("email"))
    
    storage_manager.dn_remove_data("email")
    print(storage_manager.dn_get_data("email"))  # This should print None as the email data has been removed

if __name__ == "__main__":
    dn_process_storage()