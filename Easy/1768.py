# https://leetcode.com/problems/merge-strings-alternately/description
# You are given two strings word1 and word2. Merge the strings by adding letters in
# alternating order, starting with word1. If a string is longer than the other, append 
# the additional letters onto the end of the merged string. Return the merged string.


# Using zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        for a, b in zip_longest(word1, word2, fillvalue=''):
            res.extend([a, b])

        return ''.join(res)


# Without using zip
class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        for i in range(min(len(word1), len(word2))):
            res.extend([word1[i], word2[i]])

        res.extend(word1[i + 1:])
        res.extend(word2[i + 1:])

        return ''.join(res)
      
