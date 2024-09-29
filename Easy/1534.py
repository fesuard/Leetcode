# https://leetcode.com/problems/count-good-triplets/description/
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#     0 <= i < j < k < arr.length
#     |arr[i] - arr[j]| <= a
#     |arr[j] - arr[k]| <= b
#     |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        res += 1
        return res
