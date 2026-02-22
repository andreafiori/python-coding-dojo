"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Questions: https://leetcode.com/problems/longest-common-prefix/

"""

from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs):
        ls = len(strs)
        if ls == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < ls:
                try:
                    if strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            if index == ls:
                prefix = prefix + current
            else:
                break
            pos += 1
        return prefix

    # def longestCommonPrefix(self, strs):
    #     # https://leetcode.com/discuss/89987/one-line-solution-using-itertools-takewhile
    #     return reduce(lambda s1, s2: ''.join(y[0] for y in itertools.takewhile(lambda x: x[0] == x[1], zip(s1, s2))), strs or [''])

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        strs.sort()
        first = strs[0]
        last = strs[n - 1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            else:
                res = res + first[i]
        return res

#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
#             res += strs[0][i]
#         return res

# if __name__ == '__main__':
#     # begin
#     s = Solution()
#     print s.longestCommonPrefix(["aca","cba"])