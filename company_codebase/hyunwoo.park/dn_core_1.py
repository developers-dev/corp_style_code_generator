# @dn- 코드베이스 'core' 기능과 관련된 Python 파일
# written by hyunwoo.park

class DN_Core:
    def __init__(self, name):
        self.name = name

    def dn_print_name(self):
        print(f"Name: {self.name}")


def dn_add_numbers(num1, num2):
    return num1 + num2

def dn_multiply_numbers(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    core = DN_Core("Danal")
    core.dn_print_name()

    result1 = dn_add_numbers(5, 10)
    print(f"Addition result: {result1}")

    result2 = dn_multiply_numbers(3, 7)
    print(f"Multiplication result: {result2}")