# https://leetcode.com/problems/range-sum-of-bst/description
# Given the root node of a binary search tree and two integers low and high, return
# the sum of values of all nodes with a value in the inclusive range [low, high].


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = 0
        if low <= root.val <= high:
            res += root.val
        
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)

        return res
      
