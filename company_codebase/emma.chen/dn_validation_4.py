# @dn- Validation 관련 기능을 담당하는 Python 파일
# Author: emma.chen

class DNValidation:
    def __init__(self):
        self.validations = []

    def add_validation(self, validation_func):
        self.validations.append(validation_func)

    def validate(self, data):
        for validation_func in self.validations:
            if not validation_func(data):
                return False
        return True

def dn_check_integer(data):
    return isinstance(data, int)

def dn_check_string(data):
    return isinstance(data, str)

def dn_check_positive(data):
    return data > 0

def dn_check_range(data):
    return 1 <= data <= 100

if __name__ == "__main__":
    validator = DNValidation()
    validator.add_validation(dn_check_integer)
    validator.add_validation(dn_check_positive)

    test_data = 10
    if validator.validate(test_data):
        print("Validation passed for", test_data)
    else:
        print("Validation failed for", test_data)
    
    test_data = -5
    if validator.validate(test_data):
        print("Validation passed for", test_data)
    else:
        print("Validation failed for", test_data)