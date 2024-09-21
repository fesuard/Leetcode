# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


# Solution 1:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sort_strs = sorted(strs, key=lambda x: len(x))
        n = len(sort_strs[0])
        if n == 0:
            return ""
        char = sort_strs[0][0]
        res = ""
        for i in range(n):
            pref = True
            for j in range(len(strs)):
                if sort_strs[j][i] != char:
                    pref = False
                    break
            if pref:
                res += char
                if i < n - 1:
                    char = sort_strs[0][i + 1]
            else:
                break
        return res


# Solution 2:
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sort_strs = sorted(strs)
        first = sort_strs[0]
        last = sort_strs[-1]
        res = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res
