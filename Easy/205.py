# https://leetcode.com/problems/isomorphic-strings/description
# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters
# in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving
# the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        index_s = []
        index_t = []
        for char in s:
            index_s.append(s.index(char))
        for char in t:
            index_t.append(t.index(char))
        return index_s == index_t
      
