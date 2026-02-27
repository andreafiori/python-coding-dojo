"""
Group anagrams | leetcode 49 | https://leetcode.com/problems/group-anagrams/
method: dictionary with char counter as key
"""

from collections import defaultdict

class GroupAnagrams
    def groupAnagrams(self, strs):
        strs.sort()
        hash = {}
        for s in strs:
            key = self.hash_key(s)
            try:
                hash[key].append(s)
            except KeyError:
                hash[key] = [s]
        return hash.values()

    def hash_key(self, s):
        # hash string with 26 length array
        table = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            table[index] += 1
        return str(table)

    def groupAnagrams(self, strs):
        grouped = defaultdict(list)

        for each_word in strs:
            count_of_ch = [0] * 26
            for each_ch in each_word:
                count_of_ch[ord(each_ch) - ord("a")] += 1
            grouped[tuple(count_of_ch)].append(each_word)

        return grouped.values()