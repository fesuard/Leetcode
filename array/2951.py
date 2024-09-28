# https://leetcode.com/problems/find-the-peaks/description/
# You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
# Return an array that consists of indices of peaks in the given array in any order.
# Notes:
#     A peak is defined as an element that is strictly greater than its neighboring elements.
#     The first and last elements of the array are not a peak.
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i-1] < mountain[i] and mountain[i+1] < mountain[i]:
                res.append(i)
        return res


#one liner:
class Solution1:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain)-1) if mountain[i-1] < mountain[i] and mountain[i+1] < mountain[i]]
