# https://leetcode.com/problems/sum-multiples/description
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are
# divisible by 3, 5, or 7. Return an integer denoting the sum of all numbers in the given range
# satisfying the constraint.


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(num for num in range(3, n + 1) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0)
      
