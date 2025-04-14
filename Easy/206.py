# https://leetcode.com/problems/reverse-linked-list/description
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# We will use 2 pointers, current and prev. Until is None, we traverse each node
# and make the next of the current node into the previous node. Prev becomes the
# current node, and current becomes the next node. We return prev at the end 
# since current will be None.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node
        
        return prev
      
