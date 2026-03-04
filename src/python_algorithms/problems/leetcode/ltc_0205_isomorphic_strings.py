"""
Isomorphic Strings | https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

    Explanation: The strings s and t can be made identical by:
        Mapping 'e' to 'a'.
        Mapping 'g' to 'd'.

Example 2:
    Input: s = "f11", t = "b23"
    Output: false
    Explanation: The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
    Input: s = "paper", t = "title"
    Output: true

"""

class IsomorphicStrings:
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     # check every char
    #     if len(s) != len(t):
    #         return False
    #     check = [False] * len(s)
    #     for i in range(len(s)):
    #         if check[i]:
    #             continue
    #         temp = s.count(s[i])
    #         if temp != t.count(t[i]):
    #             return False
    #         if temp >= 2:
    #             for j in range(i + 1, len(s)):
    #                 if s[j] == s[i]:
    #                     check[j] = True
    #                     if t[j] != t[i]:
    #                         return False
    #         check[i] = True
    #     return True

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        ls = len(s)
        mapStoT = [0] * 127
        mapTtoS = [0] * 127
        for i in range(ls):
            s_num, t_num = ord(s[i]), ord(t[i])
            if mapStoT[s_num] == 0 and mapTtoS[t_num] == 0:
                mapStoT[s_num] = t_num
                mapTtoS[t_num] = s_num
            elif mapTtoS[t_num] != s_num or mapStoT[s_num] != t_num:
                return False
        return True
