# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
# You are given a 0-indexed array of string words and two integers left and right.
# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = 'aeiou'
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
        return count
