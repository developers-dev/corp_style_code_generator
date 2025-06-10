#@danal- 유틸리티 기능을 제공하는 Python 파일

# 유틸리티 함수 1: 리스트 안의 모든 숫자를 합산하는 함수
def dn_sum_numbers_in_list(input_list):
    total = 0
    for num in input_list:
        if isinstance(num, (int, float)):
            total += num
    return total

# 유틸리티 함수 2: 문자열을 거꾸로 뒤집는 함수
def dn_reverse_string(input_string):
    return input_string[::-1]

# DNUtil 클래스: 유틸리티 기능을 제공하는 클래스
class DNUtil:
    def __init__(self, name):
        self.name = name

    def dn_greet(self):
        return "Hello, " + self.name + "!"

    def dn_check_palindrome(self, text):
        text = text.lower().replace(" ", "")
        return text == text[::-1]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    total = dn_sum_numbers_in_list(numbers)
    print("Total sum of numbers:", total)

    text = "hello world"
    reversed_text = dn_reverse_string(text)
    print("Reversed text:", reversed_text)

    util = DNUtil("Danal")
    greeting = util.dn_greet()
    print(greeting)

    palindrome_text = "A man a plan a canal Panama"
    is_palindrome = util.dn_check_palindrome(palindrome_text)
    if is_palindrome:
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")
            

# dn_utility_5.py

         