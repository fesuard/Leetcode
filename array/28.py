# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Given two strings needle and haystack, return the index of the first occurrence of needle in
# haystack, or -1 if needle is not part of haystack.
import re

# brute force
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1


# regex
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        m = re.search(needle, haystack)
        if m:
            return m.start()
        else:
            return -1
