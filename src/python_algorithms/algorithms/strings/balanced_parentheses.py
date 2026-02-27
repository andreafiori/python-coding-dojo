from src.python_algorithms.data_structures.stack import Stack

"""
Check if parenthesis are balanced
"""
class BalancedParentheses:
    def __init__(self):
        pass

    @staticmethod
    def check(symbol_string):
        stack = Stack()
        balanced = True
        index = 0
        strLen = len(symbol_string)

        if (strLen % 2) != 0:
            return False

        while index < strLen and balanced:
            symbol = symbol_string[index]
            if symbol == "(":
                stack.push(symbol)
            else:
                if stack.is_empty():
                    balanced = False
                else:
                    stack.pop()

            index = index + 1

        return True if balanced and stack.is_empty() else False
