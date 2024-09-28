# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray
# of arr and reverse it. You are allowed to make any number of steps. Return true if you can make arr equal to target
# or false otherwise.
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return True
        else:
            return False

