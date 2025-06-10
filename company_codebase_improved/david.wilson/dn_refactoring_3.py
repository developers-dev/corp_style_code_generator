# @dn- Refactoring Module

class DNDataRefactor:
    def __init__(self, dn_data):
        """
        Constructor for DNDataRefactor.

        Args:
            dn_data (dict): A dict containing data to be refactored.
        """
        self.dn_data = dn_data

    def dn_refactor_keys(self):
        """
        Refactor keys of the dn_data.

        Returns:
            dict: A dictionary with refactored keys.
        """
        try:
            return {f'dn_{key}': value for key, value in self.dn_data.items()}
        except Exception as e:
            print(f"An error occurred while refactoring keys: {e}")
            return {}

    def dn_refactor_values(self):
        """ 
        Refactor values of the dn_data.

        Returns:
            dict: A dictionary with refactored values.
        """
        try:
            return {key: f'dn_{value}' for key, value in self.dn_data.items()}
        except Exception as e:
            print(f"An error occurred while refactoring values: {e}")
            return {}


def dn_validate_data(dn_data):
    """
    Validate the given data.

    Args:
        dn_data (dict): A dict containing data to be validated.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    try:
        if not isinstance(dn_data, dict):
            raise ValueError("Data is not a dictionary.")

        if not all(isinstance(key, str) for key in dn_data.keys()):
            raise ValueError("All keys in data must be strings.")

        if not all(isinstance(value, str) for value in dn_data.values()):
            raise ValueError("All values in data must be strings.")

        return True
    except ValueError as e:
        print(f"Data is not valid: {e}")
        return False


def dn_process_data(dn_data):
    """
    Process the given data.

    Args:
        dn_data (dict): A dict containing data to be processed.

    Returns:
        dict: A dict containing processed data.
    """
    if dn_validate_data(dn_data):
        dn_refactor = DNDataRefactor(dn_data)
        return dn_refactor.dn_refactor_keys()
    else:
        return {}


def dn_main():
    """
    Main function to run the refactoring process.
    """
    dn_data = {'name': 'Danal', 'location': 'Seoul', 'sector': 'Technology'}
    dn_refactored_data = dn_process_data(dn_data)
    print(f"Refactored data: {dn_refactored_data}")


if __name__ == "__main__":
    dn_main()