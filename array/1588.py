# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
# Sum of All Odd Length Subarrays
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return sum(arr)
        res = sum(arr)
        for i in range(3, len(arr)+1, 2):
            pase = 0
            while i+pase <= len(arr):
                res += sum(arr[pase:i+pase])
                pase += 1
        return res
