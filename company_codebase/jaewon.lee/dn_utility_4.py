# @dn- Utility functions for Danal's codebase
# Python file for various utility functions related to Danal's codebase

# Helper function to calculate the sum of two numbers
def dn_calculate_sum(a, b):
    return a + b

# Class for working with strings
class DNStringUtil:
    def __init__(self):
        pass

    # Function to reverse a given string
    def dn_reverse_string(self, text):
        return text[::-1]

    # Function to count the number of words in a string
    def dn_count_words(self, text):
        words = text.split()
        return len(words)

# Class for mathematical operations
class DNMathUtil:
    def __init__(self):
        pass

    # Function to calculate the square of a number
    def dn_square_number(self, num):
        return num ** 2

    # Function to check if a number is prime
    def dn_is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Function to generate Fibonacci sequence up to a certain limit
def dn_generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

# Main function for testing the utility functions
def main():
    a = 10
    b = 5
    print(f"Sum of {a} and {b} is: {dn_calculate_sum(a, b)}")

    string_util = DNStringUtil()
    text = "Hello, World!"
    print(f"Reversed string: {string_util.dn_reverse_string(text)}")
    print(f"Number of words in text: {string_util.dn_count_words(text)}")

    math_util = DNMathUtil()
    num = 7
    print(f"Square of {num}: {math_util.dn_square_number(num)}")
    print(f"{num} is prime: {math_util.dn_is_prime(num)}")

    limit = 50
    print(f"Fibonacci sequence up to {limit}: {dn_generate_fibonacci(limit)}")

if __name__ == "__main__":
    main()