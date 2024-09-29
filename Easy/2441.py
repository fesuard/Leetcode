# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
# Given an integer array nums that does not contain any zeros, find the largest
# positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_nums = []
        for num in nums:
            if num > 0 and -num in nums:
                max_nums.append(num)
        return max(max_nums) if max_nums else -1
