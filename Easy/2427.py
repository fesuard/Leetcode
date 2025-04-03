# https://leetcode.com/problems/number-of-common-factors/description
# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.


# Brute force approach, we check if each number between 1 and the half of the lesser 
# number is divisible with both numbers.
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        lesser = min(a, b)
        greater = max(a, b)

        for num in range(1, lesser // 2 + 1):
            if lesser % num == 0 and greater % num == 0:
                res += 1
        
        if greater % lesser == 0:
            res += 1
        
        return res
        
