# https://leetcode.com/problems/delete-node-in-a-linked-list/description
# Given a node in a singly-linked list (excluding the head), delete it without direct 
# access to the head. The list contains unique values, and the given node is guaranteed 
# not to be the last one.
# Constraints:
# The value of the node should no longer exist in the list.
# The total number of nodes should decrease by one.
# The order of remaining nodes must be preserved.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We copy the next node's value into the given node and remove the next node
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
    
