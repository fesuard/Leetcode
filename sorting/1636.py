https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
Sort Array by Increasing Frequency
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, key=lambda x: (nums.count(x), -x))
        return sorted_nums 
