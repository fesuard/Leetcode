# https://leetcode.com/problems/unique-number-of-occurrences/description/
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or
# false otherwise.
from typing import List


# using count
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = []
        for elem in set(arr):
            res.append(arr.count(elem))
        return all(res.count(elem) == 1 for elem in res)


# using hashmap
class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashm = {}
        for elem in arr:
            hashm[elem] = hashm.get(elem, 0) + 1
        if len(set(hashm.values())) == len(hashm.values()):
            return True
        else:
            return False
