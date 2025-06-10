# @dn- Config Module
import os
import json
import sys
from typing import Any, Dict

class DNConfigError(Exception):
    """Custom exception for DNConfig related errors."""
    pass

class DNConfig:
    """A class to handle configuration management for Danal."""

    def __init__(self, dn_config_file: str):
        self.dn_config_file = dn_config_file
        self.dn_config_data = self.dn_load_config()

    def dn_load_config(self) -> Dict[str, Any]:
        """
        Load the configuration data from the config file.

        :return: A dictionary with the configuration data.
        """
        try:
            with open(self.dn_config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError as error:
            raise DNConfigError(f"Configuration file not found: {self.dn_config_file}") from error
        except json.JSONDecodeError as error:
            raise DNConfigError(f"Error parsing the configuration file: {self.dn_config_file}") from error

    def dn_get_config(self, dn_key: str) -> Any:
        """
        Get a configuration value for a given key.

        :param key: The key to get the configuration value for.
        :return: The configuration value for the key.
        """
        try:
            return self.dn_config_data[dn_key]
        except KeyError as error:
            raise DNConfigError(f"Key not found in the configuration data: {dn_key}") from error

    def dn_set_config(self, dn_key: str, dn_value: Any) -> None:
        """
        Set a configuration value for a given key.

        :param key: The key to set the configuration value for.
        :param value: The value to set.
        """
        self.dn_config_data[dn_key] = dn_value
        self.dn_save_config()

    def dn_save_config(self) -> None:
        """
        Save the current state of the configuration data to the config file.
        """
        try:
            with open(self.dn_config_file, 'w') as file:
                json.dump(self.dn_config_data, file)
        except IOError as error:
            raise DNConfigError(f"Error saving the configuration data to file: {self.dn_config_file}") from error

# Test code
def dn_test_config() -> None:
    config = DNConfig('dn_config.json')

    # Test get configuration
    try:
        print(config.dn_get_config('db_host'))
    except DNConfigError as error:
        print(error)

    # Test set configuration
    try:
        config.dn_set_config('db_host', 'localhost')
    except DNConfigError as error:
        print(error)

    # Test get configuration after setting it
    try:
        print(config.dn_get_config('db_host'))
    except DNConfigError as error:
        print(error)

if __name__ == "__main__":
    dn_test_config()