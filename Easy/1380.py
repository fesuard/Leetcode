# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix 
# in any order. A lucky number is an element of the matrix such that it is the minimum
# element in its row and maximum in its column.


# Since the elements of the matrix are unique, we first store the min elements of 
# each row. After that, we check the max of each column, if the max number of
# the column is in our min_row_elements, we add that to res.
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        min_row_elements = []
        res = []

        for row in matrix:
            min_row_elements.append(min(row))

        for i in range(m):
            max_elem = 0
            for j in range(n):
                max_elem = max(max_elem, matrix[j][i])
            
            if max_elem in min_row_elements:
                res.append(max_elem)

        return res                
