https://leetcode.com/problems/neither-minimum-nor-maximum/description/
Neither Minimum nor Maximum
Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
            if len(nums) < 3:
                return -1
            else:
                nums.remove(min(nums))
                nums.remove(max(nums))
                return nums[0]
