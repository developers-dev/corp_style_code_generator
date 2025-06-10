# @dn- Refactoring 코드베이스를 개선하기 위한 Python 파일

# 필요한 모듈 import
import os
import sys

# 리팩토링 함수 1
def dn_find_duplicates(file_path):
    """
    파일 경로에서 중복 파일을 찾아 반환하는 함수
    :param file_path: 중복을 찾을 파일 경로
    :return: 중복된 파일 리스트
    """
    files = os.listdir(file_path)
    file_dict = {}
    duplicates = []

    for file in files:
        file_name = os.path.basename(file)
        if file_name in file_dict:
            duplicates.append(file_name)
        else:
            file_dict[file_name] = file

    return duplicates

# 리팩토링 클래스 1
class DNCodeRefactor:
    def __init__(self, codebase_path):
        self.codebase_path = codebase_path

    def dn_get_file_count(self):
        """
        코드베이스 내 파일 수를 반환하는 메서드
        :return: 파일 수
        """
        files = os.listdir(self.codebase_path)
        return len(files)

# 리팩토링 함수 2
def dn_remove_empty_lines(file_path):
    """
    파일에서 빈 줄을 제거하는 함수
    :param file_path: 빈 줄을 제거할 파일 경로
    :return: None
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)

# 리팩토링 클래스 2
class DNRefactoringTool:
    def __init__(self, file_path):
        self.file_path = file_path

    def dn_replace_text(self, old_text, new_text):
        """
        파일 내 특정 문자열을 다른 문자열로 대체하는 메서드
        :param old_text: 대체할 문자열
        :param new_text: 새로운 문자열
        :return: None
        """
        with open(self.file_path, 'r') as file:
            file_data = file.read()

        file_data = file_data.replace(old_text, new_text)

        with open(self.file_path, 'w') as file:
            file.write(file_data)

# 리팩토링 함수 3
def dn_count_lines_of_code(file_path):
    """
    코드베이스 내 전체 코드 라인 수를 세는 함수
    :param file_path: 코드베이스 경로
    :return: 코드 라인 수
    """
    total_lines = 0

    for path, _, files in os.walk(file_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(path, file), 'r') as f:
                    total_lines += len(f.readlines())

    return total_lines

if __name__ == "__main__":
    codebase_path = "/path/to/codebase"
    file_path = "/path/to/file.py"

    duplicates = dn_find_duplicates(codebase_path)
    print("Duplicates found:", duplicates)

    refactor_tool = DNRefactoringTool(file_path)
    refactor_tool.dn_replace_text("old_text", "new_text")

    code_refactor = DNCodeRefactor(codebase_path)
    num_files = code_refactor.dn_get_file_count()
    print("Number of files in codebase:", num_files)

    dn_remove_empty_lines(file_path)

    total_lines = dn_count_lines_of_code(codebase_path)
    print("Total number of lines of code in codebase:", total_lines)