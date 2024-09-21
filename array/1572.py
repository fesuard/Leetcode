https://leetcode.com/problems/matrix-diagonal-sum/
Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        i = 0
        j = n-1
        while i < n:
            res += mat[i][i]
            res += mat[i][j]
            i += 1
            j -= 1
        if n % 2 != 0:
            res -= mat[n//2][n//2]
        return res


