# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description
# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest
# common divisor of them. Return the linked list after insertion. The greatest common divisor 
# of two numbers is the largest positive integer that evenly divides both numbers.


class Solution:
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur.next:
            a = cur.val
            b = cur.next.val
            added_node = ListNode(self.gcd(a, b))

            added_node.next = cur.next
            cur.next = added_node
            cur = cur.next.next
        
        return head
      
