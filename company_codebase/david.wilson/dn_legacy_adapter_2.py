# @dn- Legacy_Adapter Module

class DNLAdapter:
    """
    A class to represent an adapter for the legacy system.
    """

    def __init__(self, dn_input_system):
        """
        Constructs an adapter for the legacy system.

        :param dn_input_system: a system to be adapted
        """
        self.dn_system = dn_input_system

    def dn_adapt_data(self, dn_data):
        """
        Adapts the data to be compatible with the legacy system.

        :param dn_data: data to be adapted
        :return: adapted data
        """
        return self.dn_system.dn_process_data(dn_data)


class DNLegacySystem:
    """
    A class to represent the legacy system.
    """

    def __init__(self):
        """
        Constructs the legacy system.
        """
        self.dn_data = {}

    def dn_process_data(self, dn_data):
        """
        Processes the data according to the legacy system's requirements.

        :param dn_data: data to be processed
        :return: processed data
        """
        for dn_key, dn_value in dn_data.items():
            self.dn_data[dn_key] = self.dn_transform_value(dn_value)
        return self.dn_data

    @staticmethod
    def dn_transform_value(dn_value):
        """
        Transforms a value according to the legacy system's requirements.

        :param dn_value: value to be transformed
        :return: transformed value
        """
        return str(dn_value)


def dn_read_data(dn_file_path):
    """
    Reads data from a file.

    :param dn_file_path: path to the file
    :return: read data
    """
    with open(dn_file_path, 'r') as dn_file:
        dn_data = dn_file.read()
    return dn_data


def dn_write_data(dn_file_path, dn_data):
    """
    Writes data to a file.

    :param dn_file_path: path to the file
    :param dn_data: data to be written
    """
    with open(dn_file_path, 'w') as dn_file:
        dn_file.write(dn_data)


def dn_main():
    """
    Main function to test the legacy adapter module.
    """
    dn_legacy_system = DNLegacySystem()
    dn_adapter = DNLAdapter(dn_legacy_system)

    dn_input_data = dn_read_data('input.txt')
    dn_adapted_data = dn_adapter.dn_adapt_data(dn_input_data)

    dn_write_data('output.txt', dn_adapted_data)


if __name__ == "__main__":
    dn_main()