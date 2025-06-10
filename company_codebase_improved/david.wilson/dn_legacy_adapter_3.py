# @dn- Legacy_Adapter Module

import time


class DNAdapterError(Exception):
    """
    Error class for DNAdapter related exceptions.
    """
    def __init__(self, message):
        self.message = message


class DNAdapter:
    """
    A class to represent the legacy adapter for the Danal company.
    """
    def __init__(self, dn_system):
        self.dn_system = dn_system

    def dn_process_data(self, dn_data):
        """
        Process the given data in the legacy system style.
        """
        try:
            processed_data = self.dn_system.process(dn_data)
            return processed_data
        except Exception as e:
            raise DNAdapterError(f"An error occurred while processing the data: {e}")

    def dn_recover_from_failure(self):
        """
        Recover the system from a failure state.
        """
        try:
            self.dn_system.recover()
        except Exception as e:
            raise DNAdapterError(f"An error occurred while recovering the system: {e}")

    def dn_handle_exception(self, exception):
        """
        Handle exceptions raised in the legacy system.
        """
        print(f"Exception: {exception}")
        self.dn_recover_from_failure()


class DNSystem:
    """
    A class to represent the legacy system of the Danal company.
    """
    def __init__(self):
        self.state = 'NORMAL'

    def process(self, data):
        """
        Process the given data.
        """
        if self.state == 'FAILURE':
            raise Exception("The system is in a failure state.")
        time.sleep(1)  # Simulate processing time
        return f"Processed data: {data}"

    def recover(self):
        """
        Recover the system from a failure state.
        """
        if self.state == 'FAILURE':
            self.state = 'NORMAL'
        else:
            raise Exception("The system is not in a failure state.")


if __name__ == "__main__":
    dn_system = DNSystem()
    dn_adapter = DNAdapter(dn_system)

    try:
        print(dn_adapter.dn_process_data("Some data"))
    except DNAdapterError as e:
        dn_adapter.dn_handle_exception(e.message)

    dn_system.state = 'FAILURE'

    try:
        print(dn_adapter.dn_process_data("Some data"))
    except DNAdapterError as e:
        dn_adapter.dn_handle_exception(e.message)

    try:
        dn_adapter.dn_recover_from_failure()
    except DNAdapterError as e:
        dn_adapter.dn_handle_exception(e.message)

    try:
        print(dn_adapter.dn_process_data("Some data"))
    except DNAdapterError as e:
        dn_adapter.dn_handle_exception(e.message)