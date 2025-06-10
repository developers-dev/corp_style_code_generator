# @dn- Storage Module
# Developer: jun.kim

import os
from typing import Optional, List

class DNStorageManager:
    """Class to manage file storage in Danal application"""

    def __init__(self, storage_path: str):
        """Initializes the storage manager with the given storage path."""
        self.dn_storage_path = storage_path
        self.dn_check_and_create_path()

    def dn_check_and_create_path(self):
        """Checks if storage path exists, if not, creates the directory."""
        if not os.path.exists(self.dn_storage_path):
            os.makedirs(self.dn_storage_path)

    def dn_store_file(self, file_name: str, file_content: str):
        """Stores the file with the given content in the storage path."""
        with open(os.path.join(self.dn_storage_path, file_name), 'w') as file:
            file.write(file_content)

    def dn_retrieve_file(self, file_name: str) -> Optional[str]:
        """Retrieves the content of the file with the given name from the storage path."""
        try:
            with open(os.path.join(self.dn_storage_path, file_name), 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    def dn_delete_file(self, file_name: str) -> bool:
        """Deletes the file with the given name from the storage path."""
        try:
            os.remove(os.path.join(self.dn_storage_path, file_name))
            return True
        except FileNotFoundError:
            return False

    def dn_list_files(self) -> List[str]:
        """Lists all the files in the storage path."""
        return os.listdir(self.dn_storage_path)


# Usage example
if __name__ == "__main__":
    storage_manager = DNStorageManager('./storage')

    # Storing a file
    storage_manager.dn_store_file('test.txt', 'This is a test file.')

    # Retrieving a file
    print(storage_manager.dn_retrieve_file('test.txt'))

    # Listing all files
    print(storage_manager.dn_list_files())

    # Deleting a file
    print(storage_manager.dn_delete_file('test.txt'))

    # Checking if file is deleted
    print(storage_manager.dn_retrieve_file('test.txt'))