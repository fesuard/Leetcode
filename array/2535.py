# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
# Difference Between Element Sum and Digit Sum of an Array
# You are given a positive integer array nums.
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.
from typing import List


# using %
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digits = []
        for num in nums:
            while num >= 1:
                digits.append(int(num % 10))
                num = num / 10
        return abs(sum(digits) - sum(nums))


# using str
class Solution1:
    def differenceOfSum(self, nums: List[int]) -> int:
        digits = [int(d) for num in nums for d in str(num)]
        return abs(sum(digits) - sum(nums))
