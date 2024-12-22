# https://leetcode.com/problems/find-the-maximum-achievable-number/description
# Given two integers, num and t. A number is achievable if it can become equal to num after applying the following operation:
# Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
# Return the maximum achievable number after applying the operation at most t times.


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        res = num + (2 * t)
        return res
      
