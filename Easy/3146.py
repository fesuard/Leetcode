# https://leetcode.com/problems/permutation-difference-between-two-strings/description
# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
# The permutation difference between s and t is defined as the sum of the absolute difference between the index of 
# the occurrence of each character in s and the index of the occurrence of the same character in t.Return the 
# permutation difference between s and t.


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        index_s = {}
        index_t = {}

        for i in range(len(s)):
            index_s[s[i]] = i
            index_t[t[i]] = i

        for char in s:
            res += abs(index_s[char] - index_t[char])

        return res 
