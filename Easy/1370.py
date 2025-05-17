# https://leetcode.com/problems/increasing-decreasing-string/description
# You are given a string s. Reorder the string using the following algorithm:
# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
# Return the resulting string after reordering s using this algorithm.


# We create a frequency dictionary and a sorted list with the unique characters of s. We iterate that list
# first in ascending order, then in descending order, we add to res and decrease the frequency of the keys 
# that are still in the dict until the frequency is 0 and then we delete that key. We repeat until the 
# dictionary is empty.
class Solution:
    def sortString(self, s: str) -> str:
        letter_dict = {}
        res = []
        chars = sorted(list(set(s)))
        
        for char in s:
            letter_dict[char] = letter_dict.get(char, 0) + 1
        
        while letter_dict:
            for char in chars:
                if char in letter_dict:
                    res.append(char)
                    letter_dict[char] -= 1
                    if letter_dict[char] == 0:
                        del letter_dict[char]
            
            for char in chars[::-1]:
                if char in letter_dict:
                    res.append(char)
                    letter_dict[char] -= 1
                    if letter_dict[char] == 0:
                        del letter_dict[char]

        return ''.join(res)
