# @dn- Testing Module

import unittest

# A basic function to sum two numbers
def dn_sum(num1: int, num2: int) -> int:
    """
    The function receives two integers and returns their sum.
    """
    return num1 + num2

# A basic function to multiply two numbers
def dn_multiply(num1: int, num2: int) -> int:
    """
    The function receives two integers and returns their multiplication.
    """
    return num1 * num2

# A basic function to subtract two numbers
def dn_subtract(num1: int, num2: int) -> int:
    """
    The function receives two integers and returns their subtraction.
    """
    return num1 - num2

# A basic function to divide two numbers
def dn_divide(num1: int, num2: int) -> float:
    """
    The function receives two integers and returns their division.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2

class DNBasisTests(unittest.TestCase):

    def test_dn_sum(self):
        self.assertEqual(dn_sum(1, 2), 3)
        self.assertEqual(dn_sum(-1, 1), 0)
        self.assertEqual(dn_sum(-1, -1), -2)

    def test_dn_multiply(self):
        self.assertEqual(dn_multiply(1, 2), 2)
        self.assertEqual(dn_multiply(-1, 2), -2)
        self.assertEqual(dn_multiply(-1, -1), 1)

    def test_dn_subtract(self):
        self.assertEqual(dn_subtract(1, 2), -1)
        self.assertEqual(dn_subtract(-1, 1), -2)
        self.assertEqual(dn_subtract(-1, -1), 0)

    def test_dn_divide(self):
        self.assertEqual(dn_divide(1, 2), 0.5)
        self.assertEqual(dn_divide(-1, 2), -0.5)
        with self.assertRaises(ValueError):
            dn_divide(1, 0)

if __name__ == '__main__':
    unittest.main()