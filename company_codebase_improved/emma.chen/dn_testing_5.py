# @dn- Testing Module

import unittest
from typing import List, Any

class DNBaseTestRunner:
    """
    This is the Base Test Runner Class which all the other Test Runners will inherit
    """
    def __init__(self, dn_test_cases: List[Any]):
        self.dn_test_cases = dn_test_cases

    def dn_run_tests(self):
        for dn_test_case in self.dn_test_cases:
            dn_test_case.run()


class DNTestCase:
    """
    This is the Base Test Case Class which all the other Test Cases will inherit
    """
    def __init__(self, dn_name: str, dn_test_func):
        self.dn_name = dn_name
        self.dn_test_func = dn_test_func

    def run(self):
        try:
            self.dn_test_func()
            print(f"Test {self.dn_name} Passed!")
        except AssertionError as e:
            print(f"Test {self.dn_name} Failed! Reason: {str(e)}")


def dn_assert_equal(dn_actual, dn_expected):
    assert dn_actual == dn_expected, f"Expected {dn_expected}, but got {dn_actual}"


class DNExampleTests(unittest.TestCase):
    """
    This is an Example Test Class which shows how to use the Base Test Classes
    """
    def test_addition(self):
        dn_assert_equal(2 + 2, 4)

    def test_subtraction(self):
        dn_assert_equal(4 - 2, 2)

    def test_multiplication(self):
        dn_assert_equal(2 * 2, 4)

    def test_division(self):
        dn_assert_equal(4 / 2, 2)

    def test_modulo(self):
        dn_assert_equal(5 % 2, 1)


if __name__ == "__main__":
    dn_test_cases = [
        DNTestCase("Addition Test", DNExampleTests().test_addition),
        DNTestCase("Subtraction Test", DNExampleTests().test_subtraction),
        DNTestCase("Multiplication Test", DNExampleTests().test_multiplication),
        DNTestCase("Division Test", DNExampleTests().test_division),
        DNTestCase("Modulo Test", DNExampleTests().test_modulo),
    ]

    dn_test_runner = DNBaseTestRunner(dn_test_cases)
    dn_test_runner.dn_run_tests()