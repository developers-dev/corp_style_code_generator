'''
@dn- 
This file contains testing related functionalities for Danal project
'''

# Helper function to calculate the sum of two numbers
def dn_add(a, b):
    return a + b

# Helper function to calculate the product of two numbers
def dn_multiply(a, b):
    return a * b

# Class to perform various testing operations
class DN_Testing:
    def __init__(self, name):
        self.name = name
    
    def dn_check_even(self, num):
        if num % 2 == 0:
            return True
        else:
            return False
    
    def dn_check_prime(self, num):
        if num > 1:
            for i in range (2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

# Function to test the functionalities
def dn_run_tests():
    test_obj = DN_Testing("Emma")
    
    print("Testing the addition function:")
    result = test_obj.dn_add(5, 10)
    print(f"Result of addition: {result}")
    
    print("\nTesting the multiplication function:")
    result = test_obj.dn_multiply(3, 6)
    print(f"Result of multiplication: {result}")
    
    print("\nTesting even number check:")
    result = test_obj.dn_check_even(7)
    print(f"Is the number even? {result}")
    
    print("\nTesting prime number check:")
    result = test_obj.dn_check_prime(7)
    print(f"Is the number prime? {result}")

if __name__ == "__main__":
    dn_run_tests()
    
'''
This code snippet contains various testing functionalities such as addition, multiplication, checking even and prime numbers.
The DN_Testing class provides methods to perform these tests, while the dn_run_tests function demonstrates how to use these functionalities.
'''