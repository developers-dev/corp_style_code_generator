'''
@dn- Danal Testing Module
This module contains functions and classes related to testing for the Danal project.

Author: emma.chen
'''

# Constants
DN_TEST_STRING = "This is a test string"

# Functions
def dn_test_function_1():
    print("This is test function 1")

def dn_test_function_2(input):
    print("Test function 2 with input:", input)

# Classes
class DNTestClass1:
    def __init__(self, name):
        self.name = name

    def dn_print_name(self):
        print("Name:", self.name)

class DNTestClass2:
    def __init__(self, value):
        self.value = value

    def dn_increment_value(self):
        self.value += 1
        print("Incremented value:", self.value)

# Main
if __name__ == "__main__":
    dn_test_function_1()
    dn_test_function_2(DN_TEST_STRING)

    test_class_1 = DNTestClass1("Alice")
    test_class_1.dn_print_name()

    test_class_2 = DNTestClass2(5)
    test_class_2.dn_increment_value()
```