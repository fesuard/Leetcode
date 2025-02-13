# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
# Given a valid parentheses string s, return the nesting depth of s. The nesting 
# depth is the maximum number of nested parentheses.


class Solution:
    def maxDepth(self, s: str) -> int:
        balance = 0
        max_open = 0

        for char in s:
            if char == "(":
                balance += 1
                max_open = max(max_open, balance)

            elif char == ")":
                balance -= 1

        return max_open
