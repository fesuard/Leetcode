# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers
# are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count_per_row = []
        index_row = []
        for i in range(len(mat)):
            index_row.append(i)
        for row in mat:
            soldier_count_per_row.append(row.count(1))
        soldier_and_index = list(zip(index_row, soldier_count_per_row))
        sorted_list = sorted(soldier_and_index, key=lambda x: (x[1], x[0]))
        return list(map(lambda x: x[0], sorted_list))[:k]
