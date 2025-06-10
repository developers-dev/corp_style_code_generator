# @dn- Storage Module
# Developed by: jun.kim 
# Company: Danal

import os
import json
from typing import Any, Dict, Optional

class DNStorageException(Exception):
    """Custom exception for DNStorage errors."""
    pass

class DNStorage:
    """A simple storage class for Danal."""

    def __init__(self, storage_path: str):
        self.dn_storage_path = storage_path
        self.dn_storage_data = self.dn_load()

    def dn_load(self) -> Dict[str, Any]:
        """Load the storage data from the file."""
        if not os.path.exists(self.dn_storage_path):
            return {}
        with open(self.dn_storage_path, 'r') as f:
            return json.load(f)

    def dn_save(self) -> None:
        """Save the storage data to the file."""
        with open(self.dn_storage_path, 'w') as f:
            json.dump(self.dn_storage_data, f)

    def dn_get(self, key: str) -> Any:
        """Get a value from the storage data."""
        return self.dn_storage_data.get(key)

    def dn_set(self, key: str, value: Any) -> None:
        """Set a value in the storage data."""
        self.dn_storage_data[key] = value
        self.dn_save()

    def dn_delete(self, key: str) -> None:
        """Delete a value from the storage data."""
        if key in self.dn_storage_data:
            del self.dn_storage_data[key]
            self.dn_save()

def dn_test_storage() -> None:
    """Test the DNStorage class."""
    storage = DNStorage('test_storage.json')

    # Test setting a value
    storage.dn_set('test_key', 'test_value')
    assert storage.dn_get('test_key') == 'test_value'

    # Test deleting a value
    storage.dn_delete('test_key')
    assert storage.dn_get('test_key') is None

    # Test loading from file
    storage2 = DNStorage('test_storage.json')
    assert storage2.dn_get('test_key') is None

    print("All tests passed.")

if __name__ == "__main__":
    dn_test_storage()