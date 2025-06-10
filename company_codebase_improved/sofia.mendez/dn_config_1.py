# @dn- Config Module

import os
import json
import logging
from typing import Any, Dict, Optional

class DNConfigError(Exception):
    """ Exception raised for errors in the DNConfig class """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class DNConfig:
    """
    The DNConfig class is responsible for handling configuration management.
    """

    def __init__(self, config_path: str = './config.json'):
        self.config_path = config_path
        self.config_data = self.dn_load_config()

    def dn_load_config(self) -> Dict[str, Any]:
        """
        Load the configuration from a JSON file.
        """

        if not os.path.exists(self.config_path):
            raise DNConfigError(f"Config file does not exist: {self.config_path}")

        try:
            with open(self.config_path, 'r') as file:
                config_data = json.load(file)
        except Exception as e:
            raise DNConfigError(f"Error loading config file: {str(e)}")

        return config_data

    def dn_get_config(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get a configuration value. If the key does not exist, it returns the default value.
        """
        return self.config_data.get(key, default)

    def dn_set_config(self, key: str, value: Any) -> None:
        """
        Set a configuration value. If the key already exists, it will be updated.
        """
        self.config_data[key] = value

    def dn_save_config(self) -> None:
        """
        Save the current configuration to the JSON file.
        """
        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            raise DNConfigError(f"Error saving config file: {str(e)}")


def dn_create_logger(name: str, level: str = 'INFO') -> logging.Logger:
    """
    Create a logger with the specified name and level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def dn_log_info(logger: logging.Logger, message: str) -> None:
    """
    Log an info message using the specified logger.
    """
    logger.info(message)


def dn_log_error(logger: logging.Logger, message: str) -> None:
    """
    Log an error message using the specified logger.
    """
    logger.error(message)