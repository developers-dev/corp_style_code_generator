# @dn- User Module

from typing import Dict, Optional
import json

class DNUser:
    """
    User class for Danal.
    """
    def __init__(self, dn_id: str, dn_name: str, dn_email: str, dn_password: str):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_email = dn_email
        self.dn_password = dn_password

    def dn_to_dict(self) -> Dict[str, str]:
        """
        Convert user instance to dictionary.
        """
        return {"id": self.dn_id, "name": self.dn_name, "email": self.dn_email}

    def dn_change_password(self, dn_new_password: str):
        """
        Change the user password.
        """
        self.dn_password = dn_new_password


def dn_load_users(dn_file_path: str) -> Dict[str, DNUser]:
    """
    Load users from a json file.
    """
    dn_users = {}
    try:
        with open(dn_file_path, 'r') as dn_file:
            dn_users_data = json.load(dn_file)
            for dn_user_data in dn_users_data:
                dn_user = DNUser(dn_user_data['id'], dn_user_data['name'], dn_user_data['email'], dn_user_data['password'])
                dn_users[dn_user.dn_id] = dn_user
    except FileNotFoundError:
        print(f"File '{dn_file_path}' not found.")
    return dn_users

def dn_save_users(dn_users: Dict[str, DNUser], dn_file_path: str):
    """
    Save users to a json file.
    """
    dn_users_data = [dn_user.dn_to_dict() for dn_user in dn_users.values()]
    with open(dn_file_path, 'w') as dn_file:
        json.dump(dn_users_data, dn_file)

def dn_get_user(dn_users: Dict[str, DNUser], dn_id: str) -> Optional[DNUser]:
    """
    Get a user by id.
    """
    return dn_users.get(dn_id)

def dn_add_user(dn_users: Dict[str, DNUser], dn_user: DNUser):
    """
    Add a user.
    """
    if dn_user.dn_id in dn_users:
        print(f"User with id '{dn_user.dn_id}' already exists.")
    else:
        dn_users[dn_user.dn_id] = dn_user