https://leetcode.com/problems/unique-number-of-occurrences/description/
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = []
        for elem in set(arr):
            res.append(arr.count(elem))
        return all(res.count(elem) == 1 for elem in res)

        
