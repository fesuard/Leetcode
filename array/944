https://leetcode.com/problems/delete-columns-to-make-sorted/description/
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
You want to delete the columns that are not sorted lexicographically.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = [[] for _ in range(len(strs[0]))]
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                columns[i].append(strs[j][i])
        return sum(column != sorted(column) for column in columns)
