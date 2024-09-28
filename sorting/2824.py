https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] < target and i < j:
                    result += 1
        return result
