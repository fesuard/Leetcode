# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is
# the same. Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
# Otherwise, return false.
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        if n == 2:
            return True
        else:
            dif = abs(arr[0] - arr[1])
            for i in range(1, n-1):
                if dif != abs(arr[i] - arr[i+1]):
                    return False
            return True
