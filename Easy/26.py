# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#     Change the array nums such that the first k elements of nums contain the unique elements in the order they
#     were present in nums initially.
#     The remaining elements of nums are not important as well as the size of nums.
#     Return k.
from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


