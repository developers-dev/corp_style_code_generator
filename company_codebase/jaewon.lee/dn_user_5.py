# @dn- User Module

from typing import Dict, Optional
import hashlib

class DNUser:
    """
    DNUser class
    """

    def __init__(self, dn_name: str, dn_password: str) -> None:
        """
        Initialize the DNUser class.
        
        :param dn_name: the name of the user
        :param dn_password: the password of the user
        """
        self.dn_name = dn_name
        self.dn_password = self._encrypt_password(dn_password)
        self.dn_data: Dict[str, str] = {}
        
    def _encrypt_password(self, dn_password: str) -> str:
        """
        Encrypt the password using SHA256
        
        :param dn_password: the password to be encrypted
        :return: the encrypted password
        """
        return hashlib.sha256(dn_password.encode()).hexdigest()

    def dn_set_data(self, key: str, value: str) -> None:
        """
        Set the additional data for the user
        
        :param key: the key of the data
        :param value: the value of the data
        """
        self.dn_data[key] = value

    def dn_get_data(self, key: str) -> Optional[str]:
        """
        Get the additional data for the user
        
        :param key: the key of the data
        :return: the value of the data
        """
        return self.dn_data.get(key, None)

def dn_create_user(dn_name: str, dn_password: str) -> DNUser:
    """
    Create a new DNUser
    
    :param dn_name: the name of the user
    :param dn_password: the password of the user
    :return: the created DNUser
    """
    return DNUser(dn_name, dn_password)

def dn_set_user_data(dn_user: DNUser, key: str, value: str) -> None:
    """
    Set the additional data for the DNUser
    
    :param dn_user: the DNUser to set the data
    :param key: the key of the data
    :param value: the value of the data
    """
    dn_user.dn_set_data(key, value)

def dn_get_user_data(dn_user: DNUser, key: str) -> Optional[str]:
    """
    Get the additional data for the DNUser
    
    :param dn_user: the DNUser to get the data
    :param key: the key of the data
    :return: the value of the data
    """
    return dn_user.dn_get_data(key)

def dn_validate_user(dn_user: DNUser, dn_password: str) -> bool:
    """
    Validate the DNUser's password
    
    :param dn_user: the DNUser to validate
    :param dn_password: the password to validate
    :return: whether the password is valid
    """
    return dn_user.dn_password == dn_user._encrypt_password(dn_password)