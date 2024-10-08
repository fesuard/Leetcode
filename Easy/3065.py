# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/
# You are given a 0-indexed integer array nums, and an integer k. In one operation, you can remove one
# occurrence of the smallest element of nums. Return the minimum number of operations needed so that
# all elements of the array are greater than or equal to k.
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for num in nums:
            if num >= k:
                count += 1
        return n - count
