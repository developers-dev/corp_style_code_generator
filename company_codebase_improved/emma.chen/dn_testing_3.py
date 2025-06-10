# @dn- Testing Module
import unittest

class DNBusinessLogic:
    """Business Logic Class"""
    def __init__(self):
        self.dn_data = []

    def dn_add_data(self, data: int) -> None:
        """Function to add data"""
        if not isinstance(data, int):
            raise ValueError("Data should be integer")
        self.dn_data.append(data)

    def dn_remove_data(self, data: int) -> None:
        """Function to remove data"""
        if not isinstance(data, int):
            raise ValueError("Data should be integer")
        if data not in self.dn_data:
            raise ValueError("Data not in list")
        self.dn_data.remove(data)

    def dn_calc_average(self) -> float:
        """Function to calculate average"""
        if not self.dn_data:
            raise ValueError("No data to calculate average")
        return sum(self.dn_data) / len(self.dn_data)


class DNTesting(unittest.TestCase):
    """Unit Test Class"""
    def setUp(self):
        self.dn_business_logic = DNBusinessLogic()

    def test_dn_add_data(self):
        """Unit test for add data function"""
        self.dn_business_logic.dn_add_data(5)
        self.assertEqual(self.dn_business_logic.dn_data, [5])

        with self.assertRaises(ValueError):
            self.dn_business_logic.dn_add_data("5")

    def test_dn_remove_data(self):
        """Unit test for remove data function"""
        self.dn_business_logic.dn_add_data(5)
        self.dn_business_logic.dn_remove_data(5)
        self.assertEqual(self.dn_business_logic.dn_data, [])

        with self.assertRaises(ValueError):
            self.dn_business_logic.dn_remove_data(5)
            self.dn_business_logic.dn_remove_data("5")

    def test_dn_calc_average(self):
        """Unit test for calculate average function"""
        self.dn_business_logic.dn_add_data(5)
        self.dn_business_logic.dn_add_data(15)
        self.assertEqual(self.dn_business_logic.dn_calc_average(), 10.0)

        with self.assertRaises(ValueError):
            self.dn_business_logic = DNBusinessLogic()
            self.dn_business_logic.dn_calc_average()


if __name__ == "__main__":
    unittest.main()