# https://leetcode.com/problems/split-strings-by-separator/description/
# Given an array of strings words and a character separator, split each string in words by separator.
# Return an array of strings containing the new strings formed after the splits, excluding empty strings.
# Notes
# separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
# A split may result in more than two strings.
# The resulting strings must maintain the same order as they were initially given.
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        split_lists = [word.split(separator) for word in words]
        res = []
        for lst in split_lists:
            for word in lst:
                if word:
                    res.append(word)
        return res


# one liner:
class Solution1:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [w for word in words for w in word.split(separator) if w]
