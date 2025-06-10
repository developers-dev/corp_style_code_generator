# @dn- Testing Module

import unittest

class DNBusinessLogic:
    """
    This class represents the business logic for Danal company.
    """
    def __init__(self):
        self.dn_data = []

    def dn_add_data(self, data: str) -> None:
        """
        Add data to the internal list.

        :param data: The data to be added.
        """
        if not isinstance(data, str):
            raise ValueError('Data is not a string')
        self.dn_data.append(data)
        
    def dn_get_data(self, index: int) -> str:
        """
        Get data at a specific index.

        :param index: The index of the data.
        :return: The data at the specified index.
        """
        if index < 0 or index >= len(self.dn_data):
            raise IndexError('Index out of range')
        return self.dn_data[index]
        
    def dn_remove_data(self, index: int) -> None:
        """
        Remove data at a specific index.

        :param index: The index of the data.
        """
        if index < 0 or index >= len(self.dn_data):
            raise IndexError('Index out of range')
        self.dn_data.pop(index)

class DNBusinessLogicTest(unittest.TestCase):
    """
    This class represents the unit tests for the DNBusinessLogic class.
    """
    def setUp(self):
        self.dn_business_logic = DNBusinessLogic()

    def test_dn_add_data(self):
        self.dn_business_logic.dn_add_data('Test')
        self.assertEqual(self.dn_business_logic.dn_get_data(0), 'Test')

    def test_dn_get_data(self):
        self.dn_business_logic.dn_add_data('Test')
        self.assertEqual(self.dn_business_logic.dn_get_data(0), 'Test')
        with self.assertRaises(IndexError):
            self.dn_business_logic.dn_get_data(1)

    def test_dn_remove_data(self):
        self.dn_business_logic.dn_add_data('Test')
        self.dn_business_logic.dn_remove_data(0)
        with self.assertRaises(IndexError):
            self.dn_business_logic.dn_get_data(0)

if __name__ == '__main__':
    unittest.main()