# https://leetcode.com/problems/count-asterisk
# You are given a string s, where every two consecutive vertical bars '|' are grouped
# into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' 
# make a pair, and so forth. Return the number of '*' in s, excluding the '*' between
# each pair of '|'. Note that each '|' will belong to exactly one pair.


class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = False
        count_star = 0

        for char in s:
            if char == "|":
                pair = not pair

            if char == "*" and not pair:
                count_star += 1

        return count_star
      
