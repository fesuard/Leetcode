# https://leetcode.com/problems/minimize-string-length/description
# Given a string s, you have two types of operation:
# 1. Choose an index i in the string, and let c be the character in position i.
#   Delete the closest occurrence of c to the left of i (if exists).
# 2. Choose an index i in the string, and let c be the character in position i. 
#   Delete the closest occurrence of c to the right of i (if exists).
# Your task is to minimize the length of s by performing the above operations zero or more times.
# Return an integer denoting the length of the minimized string


# Once we figure out what the problem actually wants us to do, it's simple, we just have
# to return the length of the string with no duplicates.
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
      
