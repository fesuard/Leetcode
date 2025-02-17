# https://leetcode.com/problems/find-the-pivot-integer/description
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between
# x and n inclusively. Return the pivot integer x. If no such integer exists, return -1. It 
# is guaranteed that there will be at most one pivot index for the given input.


class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n//2, n + 1):
            if sum(range(i + 1)) == sum(range(i, n + 1)):
                return i

        return -1
