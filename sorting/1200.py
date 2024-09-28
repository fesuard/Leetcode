https://leetcode.com/problems/minimum-absolute-difference/description/
Minimum Absolute Difference
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(b - a for a, b in pairwise(arr))
        return [[a,b] for a,b in pairwise(arr) if b-a == min_diff]
