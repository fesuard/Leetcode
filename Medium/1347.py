# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
# You are given two strings of the same length s and t. In one step you can choose
# any character of t and replace it with another character.Return the minimum number
# of steps to make t an anagram of s. An Anagram of a string is a string that contains
# the same characters with a different (or the same) ordering.


# We have 2 frequency hashmaps for both our strings, and since they are of the same length, we just check
# the missing characters in string t and we add them to the result.
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        difference = 0
        hashm_s = {}
        hashm_t = {}

        for char in s:
            hashm_s[char] = hashm_s.get(char, 0) + 1
        
        for char in t:
            hashm_t[char] = hashm_t.get(char, 0) + 1

        for char in hashm_s:
            if hashm_s[char] > hashm_t.get(char, 0):
                difference += hashm_s[char] - hashm_t.get(char, 0)
        
        return difference
            
