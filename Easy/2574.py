# https://leetcode.com/problems/left-and-right-sum-differences/description/
# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        left_side = [0] * len(nums)
        left_side[0] = 0
        right_side = [0] * len(nums)
        right_side[-1] = 0
        res = []
        for i in range(1, len(nums)):
            left_side[i] = sum(nums[:i])
        for i in range(len(nums)-2, -1, -1):
            right_side[i] = sum(nums[i+1:])
        for i in range(len(nums)):
            res.append(abs(left_side[i]-right_side[i]))
        return res
