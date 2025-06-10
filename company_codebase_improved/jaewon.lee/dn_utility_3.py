# @dn- Utility Module
# author: jaewon.lee
# date: 2022-03-27

import os
import sys
import json


class DNErrorLog:
    """Custom Exception Class for Danal's application."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DNUtility:
    """Utility class for Danal's application."""

    def __init__(self):
        pass

    @staticmethod
    def dn_load_json(file_path: str) -> dict:
        """Load json file from the given file path.
        
        Args:
            file_path (str): The path of the json file.

        Returns:
            dict: The loaded json data.
        """
        try:
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            raise DNErrorLog(f"File not found: {file_path}")

    @staticmethod
    def dn_save_json(data: dict, file_path: str):
        """Save the given data to a json file.

        Args:
            data (dict): The data to save.
            file_path (str): The path of the json file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file)
        except Exception as e:
            raise DNErrorLog(f"Failed to save json file: {str(e)}")

            
def dn_compute_sum(numbers: list) -> int:
    """Compute the sum of the given list of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        int: The sum of the numbers.
    """
    try:
        return sum(numbers)
    except TypeError:
        raise DNErrorLog("Invalid input. Only integers or floats are allowed.")


def dn_validate_file_extension(file_name: str, extension: str) -> bool:
    """Validate the extension of the given file.

    Args:
        file_name (str): The name of the file.
        extension (str): The expected file extension.

    Returns:
        bool: Whether the file has the expected extension.
    """
    return file_name.endswith(extension)


def main():
    # instantiate utility class
    dn_util = DNUtility()

    # load json file
    data_file = dn_util.dn_load_json('data.json')

    # validate file extension
    if not dn_validate_file_extension('data.json', '.json'):
        raise DNErrorLog("Invalid file extension.")

    # compute sum
    total = dn_compute_sum(data_file['numbers'])

    # save the result to a json file
    dn_util.dn_save_json({'total': total}, 'result.json')


if __name__ == "__main__":
    main()