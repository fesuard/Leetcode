# https://leetcode.com/problems/pascals-triangle/description
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.


class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1, 1]]

        for _ in range(numRows - 2):
            temp = [1]
            for i in range(len(res[-1]) - 1):
                temp.append(res[-1][i] + res[-1][i + 1])
            temp.append(1)
            res.append(temp)

        return res


# Same logic as above, but writen more efficiently
class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res
      
