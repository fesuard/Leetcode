# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            status = True
            for letter in word:
                if letter not in allowed:
                    status = False
                    break
            if status:
                res += 1
        return res
