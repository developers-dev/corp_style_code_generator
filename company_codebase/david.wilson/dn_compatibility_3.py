# @dn- Compatibility Module
# @author: david.wilson

import os
import logging


class DNCompatibility:
    """
    This is a class for handling compatibility issues.

    Attributes:
        dn_filename (str): the filename to check for compatibility.
    """

    def __init__(self, dn_filename):
        self.dn_filename = dn_filename

    def dn_check_file_exists(self) -> bool:
        """
        The function to check if a file exists.

        Returns:
            bool: The return value. True for exists, False otherwise.
        """
        return os.path.isfile(self.dn_filename)

    def dn_check_file_readability(self) -> bool:
        """
        The function to check if a file is readable.

        Returns:
            bool: The return value. True for readable, False otherwise.
        """
        return os.access(self.dn_filename, os.R_OK)

    def dn_handle_file(self):
        """
        The function to handle a file, checking if it exists and is readable.

        Returns:
            str: The return message.
        """
        if not self.dn_check_file_exists():
            return "File does not exist."
        elif not self.dn_check_file_readability():
            return "File is not readable."
        else:
            return "File exists and is readable."


def dn_log_error(dn_error_message: str):
    """
    The function to log an error message.
    
    Args:
        dn_error_message (str): The error message to log.
    """
    logging.error(dn_error_message)


def dn_handle_compatibility(dn_filename: str):
    """
    The function to handle compatibility issues.

    Args:
        dn_filename (str): The filename to check for compatibility.
    """
    dn_compatibility = DNCompatibility(dn_filename)
    dn_message = dn_compatibility.dn_handle_file()
    
    if dn_message != "File exists and is readable.":
        dn_log_error(dn_message)


def dn_main():
    """
    The main function to execute the program.
    """
    dn_filename = 'data.txt'
    dn_handle_compatibility(dn_filename)


if __name__ == "__main__":
    dn_main()