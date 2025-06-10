# @dn- Storage Module

import os
from typing import Any

class DNStorageException(Exception):
    """ Custom Exception for DNStorage """
    pass

class DNStorage:
    """
    A class to represent a storage system. 
    
    Attributes:
        storage (dict): a dictionary to store data.
    """
    
    def __init__(self):
        self.dn_storage = {}

    def dn_put(self, dn_key: str, dn_value: Any) -> None:
        """
        Put a new item in the storage.
        
        Args:
            dn_key (str): The key of the item.
            dn_value (Any): The value of the item.
            
        Raises:
            DNStorageException: If the key already exists in the storage.
        """
        if dn_key in self.dn_storage:
            raise DNStorageException(f"{dn_key} already exists.")
        else:
            self.dn_storage[dn_key] = dn_value

    def dn_get(self, dn_key: str) -> Any:
        """
        Get an item from the storage by its key.
        
        Args:
            dn_key (str): The key of the item.
            
        Returns:
            The value of the item.
            
        Raises:
            DNStorageException: If the key does not exist in the storage.
        """
        try:
            return self.dn_storage[dn_key]
        except KeyError:
            raise DNStorageException(f"{dn_key} does not exist.")

    def dn_delete(self, dn_key: str) -> None:
        """
        Delete an item from the storage by its key.
        
        Args:
            dn_key (str): The key of the item.
            
        Raises:
            DNStorageException: If the key does not exist in the storage.
        """
        try:
            del self.dn_storage[dn_key]
        except KeyError:
            raise DNStorageException(f"{dn_key} does not exist.")

    def dn_update(self, dn_key: str, dn_value: Any) -> None:
        """
        Update the value of an item in the storage.
        
        Args:
            dn_key (str): The key of the item.
            dn_value (Any): The new value of the item.
            
        Raises:
            DNStorageException: If the key does not exist in the storage.
        """
        try:
            self.dn_storage[dn_key] = dn_value
        except KeyError:
            raise DNStorageException(f"{dn_key} does not exist.")

    def dn_clear(self) -> None:
        """
        Clear the storage.
        """
        self.dn_storage.clear()

# Example usage
try:
    dn_storage = DNStorage()
    dn_storage.dn_put('test_key', 'test_value')
    print(dn_storage.dn_get('test_key')) # Outputs: 'test_value'
    dn_storage.dn_update('test_key', 'new_test_value')
    print(dn_storage.dn_get('test_key')) # Outputs: 'new_test_value'
    dn_storage.dn_delete('test_key')
except DNStorageException as e:
    print(str(e))