# https://leetcode.com/problems/increasing-order-search-tree/description
# Given the root of a binary search tree, rearrange the tree in in-order so that the
# leftmost node in the  tree is now the root of the tree, and every node has no left 
# child and only one right child.


# We do an inorder traversal so we can save the values of the nodes in the correct
# order. We create the new tree's root and then we iterate throught the rest of the
# values in our list, and build the new tree by adding them to the right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        tree = TreeNode(vals[0])
        tmp = tree # We use a different variable for building the tree so we
                   # have our original root saved

        for node_val in vals[1:]:
            tmp.right = TreeNode(node_val)
            tmp = tmp.right

        return tree
      
