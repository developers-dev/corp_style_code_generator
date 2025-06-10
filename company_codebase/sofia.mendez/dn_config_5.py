# @dn- Config Module

from abc import ABC, abstractmethod
from typing import Any, Dict

# Exception Classes
class DN_ConfigError(Exception):
    """Base class for exceptions in this module."""
    pass

class DN_ConfigKeyError(DN_ConfigError):
    """Exception raised for errors in the input key."""
    def __init__(self, key):
        self.key = key
        self.message = f"Config Key '{self.key}' not found"
        super().__init__(self.message)


class DN_Config(ABC):
    """Abstract Base Class for all types of config classes."""
    
    @abstractmethod
    def dn_get_config(self, key: str) -> Any:
        pass

    @abstractmethod
    def dn_set_config(self, key: str, value: Any) -> None:
        pass

class DN_FileConfig(DN_Config):
    """Config class for file based configurations."""

    def __init__(self):
        self.dn_config_data = {}

    def dn_get_config(self, key: str) -> Any:
        """Gets the config value for the provided key."""
        if key in self.dn_config_data:
            return self.dn_config_data[key]
        else:
            raise DN_ConfigKeyError(key)

    def dn_set_config(self, key: str, value: Any) -> None:
        """Sets the config value for the provided key."""
        self.dn_config_data[key] = value

class DN_DBConfig(DN_Config):
    """Config class for database based configurations."""

    def __init__(self, db_connection):
        self.dn_db_connection = db_connection

    def dn_get_config(self, key: str) -> Any:
        """Gets the config value for the provided key."""
        query = f"SELECT value FROM config WHERE key = '{key}'"
        cursor = self.dn_db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            raise DN_ConfigKeyError(key)

    def dn_set_config(self, key: str, value: Any) -> None:
        """Sets the config value for the provided key."""
        query = f"INSERT INTO config (key, value) VALUES ('{key}', '{value}') ON DUPLICATE KEY UPDATE value = '{value}'"
        cursor = self.dn_db_connection.cursor()
        cursor.execute(query)

def dn_load_configs(config: DN_Config, config_data: Dict[str, Any]) -> None:
    """Loads the provided config data into the provided config object."""
    for key, value in config_data.items():
        config.dn_set_config(key, value)

def dn_get_config_value(config: DN_Config, key: str) -> Any:
    """Returns the config value for the provided key."""
    return config.dn_get_config(key)