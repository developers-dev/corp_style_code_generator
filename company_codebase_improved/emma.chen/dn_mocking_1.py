# @dn- Mocking Module
# dn_mocking.py

import unittest
from unittest.mock import MagicMock, patch

class DNCalculator:
    """
    A simple calculator class to demonstrate mocking in tests.
    """
    def dn_add(self, a: int, b: int) -> int:
        """
        Returns the sum of two numbers.
        """
        return a + b

    def dn_subtract(self, a: int, b: int) -> int:
        """
        Returns the subtraction of two numbers.
        """
        return a - b

    def dn_multiply(self, a: int, b: int) -> int:
        """
        Returns the multiplication of two numbers.
        """
        return a * b

    def dn_divide(self, a: int, b: int) -> float:
        """
        Returns the division of two numbers.
        """
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

class DNTestCalculator(unittest.TestCase):
    """
    A class to test the DNCalculator class using mocking.
    """
    def setUp(self):
        self.dn_calc = DNCalculator()

    def test_dn_add(self):
        """
        Test the dn_add method.
        """
        self.dn_calc.dn_add = MagicMock(return_value=5)
        result = self.dn_calc.dn_add(2, 3)
        self.dn_calc.dn_add.assert_called_with(2, 3)
        self.assertEqual(result, 5)

    def test_dn_subtract(self):
        """
        Test the dn_subtract method.
        """
        self.dn_calc.dn_subtract = MagicMock(return_value=-1)
        result = self.dn_calc.dn_subtract(2, 3)
        self.dn_calc.dn_subtract.assert_called_with(2, 3)
        self.assertEqual(result, -1)

    def test_dn_multiply(self):
        """
        Test the dn_multiply method.
        """
        self.dn_calc.dn_multiply = MagicMock(return_value=6)
        result = self.dn_calc.dn_multiply(2, 3)
        self.dn_calc.dn_multiply.assert_called_with(2, 3)
        self.assertEqual(result, 6)

    def test_dn_divide(self):
        """
        Test the dn_divide method.
        """
        self.dn_calc.dn_divide = MagicMock(return_value=0.67)
        result = self.dn_calc.dn_divide(2, 3)
        self.dn_calc.dn_divide.assert_called_with(2, 3)
        self.assertEqual(result, 0.67)

    @patch.object(DNCalculator, 'dn_divide')
    def test_dn_divide_by_zero(self, mock_dn_divide):
        """
        Test the dn_divide method for division by zero.
        """
        mock_dn_divide.side_effect = ValueError('Cannot divide by zero')
        with self.assertRaises(ValueError):
            self.dn_calc.dn_divide(2, 0)

if __name__ == "__main__":
    unittest.main()