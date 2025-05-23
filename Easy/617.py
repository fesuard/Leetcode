# https://leetcode.com/problems/merge-two-binary-trees/description
# Imagine that when you put one of them to cover the other, some nodes of the two 
# trees are overlapped while the others are not. You need to merge the two trees into
# a new binary tree. The merge rule is that if two nodes overlap, then sum node values
# up as the new value of the merged node. Otherwise, the NOT null node will be used as
# the node of the new tree.
# Return the merged tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged
      
