# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
# You are given a 0-indexed integer array nums and a target element target. A target index is an index i such
# that nums[i] == target. Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]
