# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
from typing import List


# using count
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        for num in nums:
            if nums.count(num) == n:
                return num


# using hashmap
class Solution1:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashm = {}
        n = len(nums) / 2
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        for key, value in hashm.items():
            if value == n:
                return key
