# https://leetcode.com/problems/merge-nodes-in-between-zeros/description
# You are given the head of a linked list, which contains a series of integers separated by 0's. 
# The beginning and end of the linked list will have Node.val == 0. For every two consecutive 0's,
# merge all the nodes lying in between them into a single node whose value is the sum of all the 
# merged nodes. The modified list should not contain any 0's. Return the head of the modified
# linked list.


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur.next: 
            if cur.val == 0:
                temp_sum = 0
                val_node = cur

            while cur.next.val:
                cur = cur.next
                temp_sum += cur.val
            
            val_node.val = temp_sum
            if cur.next.next:
                val_node.next = cur.next
                cur = val_node.next

            else:
                val_node.next = None
                cur = val_node

        return head
            
