# @dn- Compatibility Module

class DNCompatibility:
    """
    This class includes methods for checking and ensuring compatibility.
    """

    def __init__(self):
        """
        Initialize DNCompatibility class.
        """
        self.dn_version = '1.0'

    def dn_check_version(self, version: str) -> bool:
        """
        Check if the given version is compatible with the current system.

        :param version: The version to check.
        :return: True if compatible, False otherwise.
        """
        return self.dn_version == version

    def dn_check_system(self, system: str) -> bool:
        """
        Check if the given system is compatible with the current system.

        :param system: The system to check.
        :return: True if compatible, False otherwise.
        """
        return system.lower() in ['windows', 'mac', 'linux']

    def dn_set_version(self, version: str):
        """
        Set the system version.

        :param version: The version to set.
        """
        self.dn_version = version

    def dn_get_version(self) -> str:
        """
        Get the system version.

        :return: The system version.
        """
        return self.dn_version


def dn_convert_type(data, target_type: str):
    """
    Convert the given data to the target type if possible.

    :param data: The data to convert.
    :param target_type: The target type to convert to.
    :return: The converted data.
    """
    try:
        if target_type.lower() == 'string':
            return str(data)
        elif target_type.lower() == 'integer':
            return int(data)
        elif target_type.lower() == 'float':
            return float(data)
    except ValueError:
        return None


def dn_compare_data(data1, data2) -> bool:
    """
    Compare two data if they are the same.

    :param data1: The first data to compare.
    :param data2: The second data to compare.
    :return: True if they are the same, False otherwise.
    """
    return data1 == data2


def dn_check_data_type(data, data_type: str) -> bool:
    """
    Check if the given data is of the specified type.

    :param data: The data to check.
    :param data_type: The type to check against.
    :return: True if the data is of the specified type, False otherwise.
    """
    return type(data).__name__.lower() == data_type.lower()


def dn_parse_string(string: str) -> list:
    """
    Parse a string into a list of words.

    :param string: The string to parse.
    :return: A list of words in the string.
    """
    return string.split()