# @dn- 백엔드 개발자 Jin Park
# Validation 관련 기능을 위한 Python 파일

class DN_Validator:
    def __init__(self):
        self.rules = {}

    def add_rule(self, key, validation_func):
        self.rules[key] = validation_func

    def validate(self, data):
        errors = {}
        for key, rule in self.rules.items():
            if not rule(data.get(key)):
                errors[key] = f"{key} is invalid"
        return errors

def dn_is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def dn_is_email(value):
    if "@" in value:
        return True
    return False

def dn_min_length(length):
    def validation_func(value):
        if len(value) >= length:
            return True
        return False
    return validation_func

validator = DN_Validator()
validator.add_rule('age', dn_is_integer)
validator.add_rule('email', dn_is_email)
validator.add_rule('name', dn_min_length(5))

data = {'age': '25', 'email': 'test@example.com', 'name': 'Jin'}
errors = validator.validate(data)
print(errors)