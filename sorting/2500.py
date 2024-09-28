https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
Delete Greatest Value in Each Row
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        deleted_elem_sum = 0
        for elem in grid:
            elem.sort()
        while len(grid[0]) > 0:
            deleted_elem_list = []
            for elem in grid:
                deleted_elem_list.append(elem.pop(0))
            deleted_elem_sum += max(deleted_elem_list)
        return deleted_elem_sum
