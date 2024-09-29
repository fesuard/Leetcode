# https://leetcode.com/problems/sort-array-by-parity/description/
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the
# odd integers. Return any array that satisfies this condition.
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums, key=lambda x: x % 2)
        return sorted_list
