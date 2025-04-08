# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group 
# of children is separated by the null value (See examples)


# We use a depth first search function to recursively call dfs for
# each child of the current node.
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []

        def dfs(root):
            for node in root.children:
                dfs(node)
            res.append(root.val)

        dfs(root)

        return res
      
