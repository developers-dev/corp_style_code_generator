# @dn- QA 엔지니어 Emma Chen
# This Python file contains testing-related functionalities for Danal codebase

# Function to test if two numbers are equal
def dn_test_equal(a, b):
    if a == b:
        print("Test Passed: {} is equal to {}".format(a, b))
    else:
        print("Test Failed: {} is not equal to {}".format(a, b))

# Class to perform various testing operations
class DN_Testing:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
    
    # Method to run a test
    def dn_run_test(self, test_func, *args):
        self.tests_run += 1
        try:
            test_func(*args)
            self.tests_passed += 1
        except Exception as e:
            print("Test Failed with error: {}".format(e))
    
    # Method to display test results
    def dn_display_results(self):
        print("Tests Run: {}".format(self.tests_run))
        print("Tests Passed: {}".format(self.tests_passed))
        print("Tests Failed: {}".format(self.tests_run - self.tests_passed))

# Function to test if a given string is palindrome
def dn_test_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print("Test Passed: {} is a palindrome".format(s))
    else:
        print("Test Failed: {} is not a palindrome".format(s))

# Function to test if a given number is prime
def dn_test_prime(num):
    if num < 2:
        print("Test Failed: {} is not a prime number".format(num))
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Test Failed: {} is not a prime number".format(num))
            return
    print("Test Passed: {} is a prime number".format(num))

# Main function to demonstrate testing functionalities
def main():
    test = DN_Testing()
    test.dn_run_test(dn_test_equal, 5, 5)
    test.dn_run_test(dn_test_equal, 5, 10)
    test.dn_run_test(dn_test_palindrome, "radar")
    test.dn_run_test(dn_test_palindrome, "hello")
    test.dn_run_test(dn_test_prime, 7)
    test.dn_run_test(dn_test_prime, 10)
    
    test.dn_display_results()

if __name__ == "__main__":
    main()