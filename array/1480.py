# https://leetcode.com/problems/running-sum-of-1d-array/description/
# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums)+1):
            result.append(sum(nums[:i]))
        return result
