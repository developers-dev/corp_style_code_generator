# @dn- Refactoring Module

class DNRefactorer:
    """This class is a refactoring helper for Danal's legacy system."""

    def __init__(self, dn_code_base):
        """
        Initializes DNRefactorer with a code base.
        
        :param dn_code_base: A string of the code base to refactor.
        """
        self.dn_code_base = dn_code_base

    def dn_get_line_count(self) -> int:
        """
        Returns the line count of the code base.
        
        :return: The number of lines in the code base.
        """
        return len(self.dn_code_base.split('\n'))

    def dn_get_function_count(self) -> int:
        """
        Returns the function count in the code base.
        
        :return: The number of functions in the code base.
        """
        return self.dn_code_base.count('def ')

    def dn_get_class_count(self) -> int:
        """
        Returns the class count in the code base.
        
        :return: The number of classes in the code base.
        """
        return self.dn_code_base.count('class ')

    def dn_replace_old_style_print(self) -> None:
        """
        Replaces all old style print statements with new style print functions.
        """
        self.dn_code_base = self.dn_code_base.replace('print ', 'print(')
        self.dn_code_base = self.dn_code_base.replace('\n', ')\n')

    def dn_refactor(self) -> str:
        """
        Performs a series of refactoring operations on the code base.
        
        :return: The refactored code base.
        """
        self.dn_replace_old_style_print()
        return self.dn_code_base


def dn_execute_refactoring(dn_code_base: str) -> str:
    """
    Executes a refactoring process on a given code base.
    
    :param dn_code_base: A string of the code base to refactor.
    :return: The refactored code base.
    """
    dn_refactorer = DNRefactorer(dn_code_base)
    return dn_refactorer.dn_refactor()


def dn_get_refactoring_summary(dn_code_base: str) -> str:
    """
    Returns a summary of the refactoring process.
    
    :param dn_code_base: A string of the code base to refactor.
    :return: A summary string of the refactoring process.
    """
    dn_refactorer = DNRefactorer(dn_code_base)
    summary = f'Lines: {dn_refactorer.dn_get_line_count()}\n'
    summary += f'Functions: {dn_refactorer.dn_get_function_count()}\n'
    summary += f'Classes: {dn_refactorer.dn_get_class_count()}\n'
    return summary


if __name__ == '__main__':
    dn_code_base = 'def hello():\n  print "Hello, world!"\n\nclass Test:\n  def test():\n    print "Test"'
    print(dn_get_refactoring_summary(dn_code_base))
    print(dn_execute_refactoring(dn_code_base))