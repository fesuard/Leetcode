# https://leetcode.com/problems/majority-element/description
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        one_nums = list(set(nums))
        n = len(nums)
        for num in one_nums:
            if nums.count(num) > n / 2:
                return num


# hashmap:
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for key, value in d.items():
            if value > n//2:
                return key
