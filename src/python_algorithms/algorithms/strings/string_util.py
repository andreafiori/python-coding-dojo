"""
String Utils
"""
class StringUtil:
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(string):
        return str(string) == str(string)[::-1]

    @staticmethod
    def reverse(string):
        return string[::-1]
