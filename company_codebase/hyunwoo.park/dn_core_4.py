# @dn- Danal Core Functionality Python File
# Written by hyunwoo.park

# Constants
DN_MAX_VALUE = 100
DN_MIN_VALUE = 0

# Functions
def dn_add_values(a, b):
    """
    Add two values together. 
    Args:
        a (int): First value
        b (int): Second value
    Returns:
        int: Sum of a and b
    """
    return a + b

def dn_check_range(value):
    """
    Check if a value is within the acceptable range.
    Args:
        value (int): The value to be checked
    Returns:
        bool: True if value is within range, False otherwise
    """
    return DN_MIN_VALUE <= value <= DN_MAX_VALUE

# Classes
class DNUser:
    def __init__(self, name):
        self.name = name

    def dn_greet(self):
        """
        Greet the user.
        """
        print(f"Hello, {self.name}!")

class DNCalculator:
    def __init__(self):
        self.result = 0

    def dn_add_to_result(self, value):
        """
        Add a value to the current result.
        Args:
            value (int): The value to add
        """
        self.result += value

    def dn_get_result(self):
        """
        Get the current result.
        Returns:
            int: The current result
        """
        return self.result

# Main Program
if __name__ == "__main__":
    user1 = DNUser("Alice")
    user1.dn_greet()

    calc = DNCalculator()
    calc.dn_add_to_result(10)
    calc.dn_add_to_result(20)
    print(f"Final Result: {calc.dn_get_result()}")