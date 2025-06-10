# @dn- User Module

import datetime
from typing import List, Dict, Optional

class DNUserException(Exception):
    """
    User-related exception class.
    """
    pass

class DNUser:
    """
    User class defining the structure of a user.
    """
    def __init__(self, dn_id: str, dn_name: str, dn_email: str):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_email = dn_email
        self.dn_created_at = datetime.datetime.now()

    def __str__(self):
        return f'User(id={self.dn_id}, name={self.dn_name}, email={self.dn_email}, created_at={self.dn_created_at})'


class DNUserManager:
    """
    User manager class handling user-related operations.
    """
    def __init__(self):
        self.dn_users: Dict[str, DNUser] = {}

    def dn_create_user(self, dn_id: str, dn_name: str, dn_email: str) -> DNUser:
        """
        Create a new user.
        """
        if dn_id in self.dn_users:
            raise DNUserException(f'User with id {dn_id} already exists.')
        user = DNUser(dn_id, dn_name, dn_email)
        self.dn_users[dn_id] = user
        return user

    def dn_get_user(self, dn_id: str) -> Optional[DNUser]:
        """
        Retrieve a user by id.
        """
        return self.dn_users.get(dn_id, None)

    def dn_update_user(self, dn_id: str, dn_name: Optional[str] = None, dn_email: Optional[str] = None) -> DNUser:
        """
        Update the information of a user.
        """
        user = self.dn_get_user(dn_id)
        if user is None:
            raise DNUserException(f'User with id {dn_id} does not exist.')
        if dn_name is not None:
            user.dn_name = dn_name
        if dn_email is not None:
            user.dn_email = dn_email
        return user

    def dn_delete_user(self, dn_id: str) -> bool:
        """
        Delete a user by id.
        """
        if dn_id not in self.dn_users:
            raise DNUserException(f'User with id {dn_id} does not exist.')
        del self.dn_users[dn_id]
        return True

    def dn_get_all_users(self) -> List[DNUser]:
        """
        Retrieve all users.
        """
        return list(self.dn_users.values())

def dn_test_user_module():
    """
    Test function demonstrating the usage of the user module.
    """
    user_manager = DNUserManager()
    user_manager.dn_create_user('1', 'John', 'john@danal.com')
    user_manager.dn_create_user('2', 'Jane', 'jane@danal.com')
    user_manager.dn_create_user('3', 'Doe', 'doe@danal.com')

    print(user_manager.dn_get_user('1'))
    print(user_manager.dn_get_all_users())

    user_manager.dn_update_user('1', 'John Doe', 'johndoe@danal.com')
    print(user_manager.dn_get_user('1'))

    user_manager.dn_delete_user('1')
    print(user_manager.dn_get_all_users())

if __name__ == '__main__':
    dn_test_user_module()