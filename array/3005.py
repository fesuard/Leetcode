# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
from typing import List


# using count
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_list = []
        for num in nums:
            freq_list.append(nums.count(num))
        num_and_freq = zip(nums, freq_list)
        res = filter(lambda x: x[1] == max(freq_list), num_and_freq)
        return len(list(res))


# hashmap
class Solution1:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashm = {}
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        return sum(freq for freq in hashm.values() if freq == max(hashm.values()))
