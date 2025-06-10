# @dn- User Module

from typing import List, Dict, Any, Optional
import datetime

class DNUser:
    """
    DNUser class represents a user in the system.
    """
    def __init__(self, dn_id: int, dn_name: str, dn_email: str, dn_password: str, 
                 dn_created_at: datetime.datetime):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_email = dn_email
        self.dn_password = dn_password
        self.dn_created_at = dn_created_at

    def dn_to_dict(self) -> Dict[str, Any]:
        """
        Convert the user's information into a dictionary.
        """
        return {
            'id': self.dn_id,
            'name': self.dn_name,
            'email': self.dn_email,
            'password': self.dn_password,
            'created_at': self.dn_created_at,
        }


def dn_get_user(dn_id: int) -> Optional[DNUser]:
    """
    Retrieve a user from the database by their id.
    If the user does not exist, return None.
    """
    # Fetch user from database
    # This is a mocked function, replace it with real database query
    user_data = {
        'id': dn_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'password': 'password',
        'created_at': datetime.datetime.now(),
    }
    
    return DNUser(**user_data)


def dn_create_user(dn_name: str, dn_email: str, dn_password: str) -> DNUser:
    """
    Create a new user with the given information.
    """
    # Insert user into database
    # This is a mocked function, replace it with real database query
    dn_id = 1  # This should be replaced with actual id from database
    dn_created_at = datetime.datetime.now()
    
    new_user = DNUser(dn_id, dn_name, dn_email, dn_password, dn_created_at)
    
    return new_user


def dn_update_user(dn_id: int, dn_name: str, dn_email: str, dn_password: str) -> Optional[DNUser]:
    """
    Update the information of an existing user.
    If the user does not exist, return None.
    """
    # Fetch user from database
    user = dn_get_user(dn_id)
    
    if not user:
        return None
    
    # Update user's information
    user.dn_name = dn_name
    user.dn_email = dn_email
    user.dn_password = dn_password
    
    return user


def dn_delete_user(dn_id: int) -> bool:
    """
    Delete a user from the database.
    If the deletion was successful, return True.
    If the user does not exist, return False.
    """
    # Fetch user from database
    user = dn_get_user(dn_id)
    
    if not user:
        return False
    
    # Delete user
    # This is a mocked function, replace it with real database operation
    return True