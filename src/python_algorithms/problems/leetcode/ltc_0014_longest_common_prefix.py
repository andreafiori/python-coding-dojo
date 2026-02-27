"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Questions: https://leetcode.com/problems/longest-common-prefix/

"""

from typing import List

class LongestCommonPrefix:
    def find(self, strs):
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

    # def find2(self, strs):
    #     # https://leetcode.com/discuss/89987/one-line-solution-using-itertools-takewhile
    #     return reduce(lambda s1, s2: ''.join(y[0] for y in itertools.takewhile(lambda x: x[0] == x[1], zip(s1, s2))), strs or [''])

    def find3(self, strs: List[str]) -> str:
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

#     s = Solution()
#     print s.longestCommonPrefix(["aca","cba"])