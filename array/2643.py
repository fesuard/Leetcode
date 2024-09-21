https://leetcode.com/problems/row-with-maximum-ones/description/
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains 
the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the 
smallest row number should be selected.
Return an array containing the index of the row, and the number of ones in it.

#using sorted:
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        sorted_ones = sorted(enumerate(mat), key=lambda x:(-x[1].count(1), x[0]))
        return [sorted_ones[0][0], sorted_ones[0][1].count(1)]

#adding index, and 1 count in a separate list, and return the max value based on the 1 count:
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count_1_idx = []
        for i, row in enumerate(mat):
            count_1_idx.append([i, row.count(1)])
        return max(count_1_idx, key=lambda x: x[1])
