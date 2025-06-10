# @dn- Config Module
import os
import json
from typing import Any, Dict


class DNConfigError(Exception):
    """Custom exception for DNConfig related errors"""
    pass


class DNConfig:
    """A simple configuration management class"""

    def __init__(self, config_file: str) -> None:
        """
        Initialize DNConfig with a configuration file

        :param config_file: path to the configuration file
        """
        self.config_file = config_file
        self.config = self.dn_load_config()

    def dn_load_config(self) -> Dict[str, Any]:
        """
        Load configuration from a json file

        :return: a dictionary with the loaded configuration
        """
        if not os.path.exists(self.config_file):
            raise DNConfigError(f"Config file {self.config_file} does not exist")

        with open(self.config_file, 'r') as fp:
            try:
                config = json.load(fp)
            except json.JSONDecodeError:
                raise DNConfigError(f"Error decoding config file {self.config_file}")

        return config

    def dn_get_config(self, key: str) -> Any:
        """
        Get a configuration value

        :param key: the key for the configuration value
        :return: the configuration value
        """
        return self.config.get(key)

    def dn_set_config(self, key: str, value: Any) -> None:
        """
        Set a configuration value

        :param key: the key for the configuration value
        :param value: the new value for the key
        """
        self.config[key] = value

    def dn_save_config(self) -> None:
        """
        Save the current config to the config file
        """
        with open(self.config_file, 'w') as fp:
            json.dump(self.config, fp, indent=4)


def dn_create_default_config(file_path: str) -> None:
    """
    Create a default configuration file

    :param file_path: path for the new configuration file
    """
    default_config = {
        'host': 'localhost',
        'port': 8000,
        'debug': True
    }

    with open(file_path, 'w') as fp:
        json.dump(default_config, fp, indent=4)


def dn_update_config_file(config: DNConfig, key: str, value: Any) -> None:
    """
    Update a configuration value in the configuration file

    :param config: a DNConfig instance
    :param key: the key for the configuration value
    :param value: the new value for the key
    """
    config.dn_set_config(key, value)
    config.dn_save_config()


def dn_print_config(config: DNConfig) -> None:
    """
    Print the current configuration

    :param config: a DNConfig instance
    """
    for key, value in config.config.items():
        print(f"{key}: {value}")