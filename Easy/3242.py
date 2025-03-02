# https://leetcode.com/problems/design-neighbor-sum-service/description
# You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].
# Implement the NeighborSum class:
# NeighborSum(int [][]grid) initializes the object.
# int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, 
# that is either to the top, left, right, or bottom of value in grid.
# int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, 
# that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.values_index = {grid[i][j] : (i,j) for i in range(self.n) for j in range(self.n)}

    def adjacentSum(self, value: int) -> int:
        i, j = self.values_index[value]
        adj_values = ((i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j))
        adj_sum = 0

        for a, b in adj_values:
            if a in range(self.n) and b in range(self.n):
                adj_sum += self.grid[a][b]

        return adj_sum
        
    def diagonalSum(self, value: int) -> int:
        i, j = self.values_index[value]
        adj_values = ((i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1))
        diag_sum = 0

        for a, b in adj_values:
            if a in range(self.n) and b in range(self.n):
                diag_sum += self.grid[a][b]

        return diag_sum
        

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
