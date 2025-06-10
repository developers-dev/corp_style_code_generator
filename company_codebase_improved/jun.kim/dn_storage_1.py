# @dn- Storage Module

from typing import Any, List, Dict

class DNStorage:
    """A simple storage class for Danal's mobile application."""

    def __init__(self):
        self.dn_data = {}

    def dn_add(self, key: str, value: Any) -> None:
        """Add a new item to the storage."""
        self.dn_data[key] = value

    def dn_get(self, key: str) -> Any:
        """Get an item from the storage."""
        return self.dn_data.get(key)

    def dn_update(self, key: str, value: Any) -> None:
        """Update an item in the storage."""
        if key in self.dn_data:
            self.dn_data[key] = value

    def dn_remove(self, key: str) -> None:
        """Remove an item from the storage."""
        if key in self.dn_data:
            del self.dn_data[key]


def dn_get_all(storage: DNStorage) -> Dict[str, Any]:
    """Get all items from the storage."""
    return storage.dn_data

def dn_clear_all(storage: DNStorage) -> None:
    """Clear all items from the storage."""
    storage.dn_data.clear()

def dn_get_keys(storage: DNStorage) -> List[str]:
    """Get all keys from the storage."""
    return list(storage.dn_data.keys())

def dn_get_values(storage: DNStorage) -> List[Any]:
    """Get all values from the storage."""
    return list(storage.dn_data.values())

# Example usage
dn_storage = DNStorage()
dn_storage.dn_add('username', 'jun.kim')
dn_storage.dn_add('email', 'jun.kim@danal.com')

print(dn_get_all(dn_storage))  # {'username': 'jun.kim', 'email': 'jun.kim@danal.com'}
print(dn_get_keys(dn_storage))  # ['username', 'email']
print(dn_get_values(dn_storage))  # ['jun.kim', 'jun.kim@danal.com']

dn_storage.dn_update('username', 'jun.kim2')
print(dn_get_all(dn_storage))  # {'username': 'jun.kim2', 'email': 'jun.kim@danal.com'}

dn_storage.dn_remove('username')
print(dn_get_all(dn_storage))  # {'email': 'jun.kim@danal.com'}

dn_clear_all(dn_storage)
print(dn_get_all(dn_storage))  # {}