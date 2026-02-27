"""
"""

class FindTheDifference:
    def find(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ord(t[-1])
        for i in range(len(s)):
            res += ord(t[i])
            res -= ord(s[i])
        return chr(res)

    # def find(self, s, t):
    #     res = 0
    #     for c in s + t:
    #         res ^= ord(c)
    #     return chr(res)
