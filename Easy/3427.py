# https://leetcode.com/problems/sum-of-variable-length-subarrays/description
# You are given an integer array nums of size n. For each index i where 0 <= i < n, define a 
# subarray nums[start ... i] where start = max(0, i - nums[i]). Return the total sum of all
# elements from the subarray defined for each index in the array.


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum_total = 0

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            sum_total += sum(nums[start : i + 1])

        return sum_total
