# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
# Largest Local Values in a Matrix
# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        while i+3 <= len(grid):  
            j = 0
            max_list = []
            while j+3 <= len(grid):
                max_val = 0
                max_val = max(max(grid[i][j:j+3]), max_val)
                max_val = max(max(grid[i+1][j:j+3]), max_val)
                max_val = max(max(grid[i+2][j:j+3]), max_val)
                max_list.append(max_val)
                j += 1
            res.append(max_list)
            i += 1
        return res
                


            
