https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/
Subarrays Distinct Element Sum of Squares I
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarray_list = []
        for i in range(len(nums)):
            j=i
            while j < len(nums):
                subarray_list.append(nums[i:j+1])
                j += 1
        return sum((len(set(sub))**2 for sub in subarray_list))
