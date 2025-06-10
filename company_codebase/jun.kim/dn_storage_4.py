# @dn- Storage Module

from typing import Any, Dict, Optional

class DNStorageError(Exception):
    """A general error class for DNStorage."""
    
class DNNotFoundError(DNStorageError):
    """An error class for when a key is not found in storage."""

class DNStorage:
    """A simple storage class for the Danal project."""
    def __init__(self):
        self.dn_data: Dict[str, Any] = {}

    def dn_add(self, key: str, value: Any) -> None:
        """
        This method adds a key-value pair to the storage.

        :param key: The key to be added to the storage.
        :param value: The value to be associated with the key.
        """
        self.dn_data[key] = value

    def dn_get(self, key: str) -> Any:
        """
        This method retrieves a value associated with a key from the storage.

        :param key: The key to retrieve the value for.
        :return: The value associated with the key.
        :raises DNNotFoundError: If the key is not found in the storage.
        """
        if key in self.dn_data:
            return self.dn_data[key]
        else:
            raise DNNotFoundError(f"'{key}' not found in storage.")

    def dn_update(self, key: str, value: Any) -> None:
        """
        This method updates the value associated with a key in the storage.

        :param key: The key to update the value for.
        :param value: The new value to be associated with the key.
        :raises DNNotFoundError: If the key is not found in the storage.
        """
        if key in self.dn_data:
            self.dn_data[key] = value
        else:
            raise DNNotFoundError(f"'{key}' not found in storage.")

    def dn_delete(self, key: str) -> None:
        """
        This method deletes a key-value pair from the storage.

        :param key: The key to delete along with its associated value.
        :raises DNNotFoundError: If the key is not found in the storage.
        """
        if key in self.dn_data:
            del self.dn_data[key]
        else:
            raise DNNotFoundError(f"'{key}' not found in storage.")


def dn_process_data(storage: DNStorage, actions: Dict[str, Any]) -> None:
    """
    This function processes a series of actions on a DNStorage instance.

    :param storage: The DNStorage instance to perform actions on.
    :param actions: A dictionary of actions to perform.
    """
    for action, params in actions.items():
        if action == 'add':
            storage.dn_add(params['key'], params['value'])
        elif action == 'update':
            storage.dn_update(params['key'], params['value'])
        elif action == 'get':
            try:
                print(storage.dn_get(params['key']))
            except DNNotFoundError as e:
                print(e)
        elif action == 'delete':
            try:
                storage.dn_delete(params['key'])
            except DNNotFoundError as e:
                print(e)

def main():
    dn_storage = DNStorage()
    actions = {
        'add': {'key': 'username', 'value': 'jun.kim'},
        'get': {'key': 'username'},
        'update': {'key': 'username', 'value': 'danal.jun.kim'},
        'get': {'key': 'username'},
        'delete': {'key': 'username'},
        'get': {'key': 'username'},
    }
    dn_process_data(dn_storage, actions)


if __name__ == '__main__':
    main()