# https://leetcode.com/problems/reverse-degree-of-a-string/description
# Given a string s, calculate its reverse degree.
# The reverse degree is calculated as follows:
# For each character, multiply its position in the reversed alphabet ('a' = 26,
# 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
# Sum these products for all characters in the string.
# Return the reverse degree of s.


# We create a dictionary with the letters as keys, and with their respective
# degrees as values. After that we do a for loop for the characters in our s
# string, for each character we multiply the given index with the value of our
# dictionary.
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        letter_degree = dict()
        degree = 26

        for i in range(97, 124):
            letter_degree[chr(i)] = degree
            degree -= 1

        for i, char in enumerate(s):
            res += (i + 1) * letter_degree[char]
        
        return res
      
