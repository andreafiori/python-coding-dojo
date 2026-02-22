"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Question: https://leetcode.com/problems/valid-parentheses/

"""

class Solution:
    def solution_one(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        stack = []
        for t in s:
            if t == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif t == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                stack.append(t)
        if len(stack) == 0:
            return True
        else:
            return False


    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False

    def solution_two(self, s: str) -> bool:
        para = {')': '(', ']': '[', '}': '{'}
        op = ['(', '[', '{']
        stack = []

        for c in s:
            if c in op:
                stack.append(c)

            elif c in para:
                if len(stack) != 0 and stack[-1] == para[c]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False