# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [elem ** 2 for elem in nums]
        nums.sort()
        return nums
