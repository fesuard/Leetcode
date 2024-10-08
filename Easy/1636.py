# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.
from typing import List


# using sorted and count
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, key=lambda x: (nums.count(x), -x))
        return sorted_nums 


# hashmap
class Solution1:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashm = {}
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        freq = list(hashm.items())
        freq = sorted(freq, key=lambda x: (x[1], -x[0]))
        res = []
        for a, b in freq:
            res.extend([a] * b)
        return res
