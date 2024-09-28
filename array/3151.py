# https://leetcode.com/problems/special-array-i/description/
# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
from typing import List


# using zip
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            for a, b in zip(nums, nums[1:]):
                if a % 2 == b % 2:
                    return False
        return True


# using for
class Solution1:
    def isArraySpecial(self, nums: List[int]) -> bool:
        res = True
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                res = False
                break
        return res
