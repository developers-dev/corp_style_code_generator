# @dn- Danal UI Component Python File
#
# This file contains the implementation of various UI components for Danal's codebase.

class DNButton:
    def __init__(self, text):
        self.text = text

    def click(self):
        print(f'Button clicked: {self.text}')

def dn_create_button(text):
    return DNButton(text)

class DNInput:
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def get_input(self):
        return input(f'Enter text ({self.placeholder}): ')

def dn_create_input(placeholder):
    return DNInput(placeholder)

if __name__ == '__main__':
    button = dn_create_button('Click me')
    button.click()

    input_field = dn_create_input('Enter your name')
    user_input = input_field.get_input()
    print(f'User input: {user_input}')