# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
# You are given an m x n matrix grid consisting of positive integers.Perform the following operation until grid
# becomes empty:
# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        deleted_elem_sum = 0
        for row in grid:
            row.sort()
        for _ in range(len(grid[0])):
            deleted_elem_list = []
            for row in grid:
                deleted_elem_list.append(row.pop())
            deleted_elem_sum += max(deleted_elem_list)
        return deleted_elem_sum
