# @dn- QA Engineer: Emma Chen
# Python file for testing related functionalities

# Importing necessary libraries
import pytest

# Function to add two numbers
def dn_add_numbers(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def dn_multiply_numbers(num1, num2):
    return num1 * num2

# Class for testing math functions
class DNMathTest:
    def __init__(self):
        self.num1 = 5
        self.num2 = 10

    def test_addition(self):
        result = dn_add_numbers(self.num1, self.num2)
        assert result == 15

    def test_multiplication(self):
        result = dn_multiply_numbers(self.num1, self.num2)
        assert result == 50

# Function to check if a number is odd or even
def dn_check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to test odd or even functionality
def test_odd_even():
    assert dn_check_odd_even(4) == "Even"
    assert dn_check_odd_even(5) == "Odd"

if __name__ == "__main__":
    pytest.main()