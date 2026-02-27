"""

"""

class ValidPalindrome:
    def isPalindrome(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        alnum_s = [s.lower() for t in s if s.isalnum()]
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls / 2
        for i in range(mid):
            if alnum_s[i] != alnum_s[ls - 1 - i]:
                return False
        return True
