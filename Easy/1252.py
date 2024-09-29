# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/
# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each
# indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
#     Increment all the cells on row ri.
#     Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all
# locations in indices.
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = []
        for i in range(m):
            mat.append([0] * n)
        for indice in indices:
            mat[indice[0]] = [i+1 for i in mat[indice[0]]]
            for c in mat:
                c[indice[1]] += 1
        return sum(1 if elem % 2 != 0 else 0 for row in mat for elem in row)
