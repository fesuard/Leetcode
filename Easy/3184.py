# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description
# Given an integer array hours representing times in hours, return an integer denoting
# the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.


# Brute force approach, we iterate through each pair of elements of our list and
# check if they divide evenly with 24.
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        n = len(hours)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    res += 1

        return res
      
