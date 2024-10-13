# https://leetcode.com/problems/valid-anagram/description
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# using sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hashm = {}
            for char in s:
                if char in hashm:
                    hashm[char] += 1
                else:
                    hashm[char] = 1
            for char in t:
                if char in hashm:
                    hashm[char] -= 1
                else:
                    hashm[char] = -1
            for value in hashm.values():
                if value != 0:
                    return False
            return True
        return False
