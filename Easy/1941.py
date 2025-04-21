# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description
# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same 
# number of occurrences (i.e., the same frequency).


# We create a frequency hashmap, and if the length of the set of the values for that hashmap
# is equal to 1, that means all of the frequencies would be 1 so we return True.
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hmap = dict()

        for char in s:
            hmap[char] = hmap.get(char, 0) + 1

        return len(set(hmap.values())) == 1
      
