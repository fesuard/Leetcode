# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/description
# You are given an immutable linked list, print out all values of each node in reverse with the
# help of the following interface:
# ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
# You need to use the following functions to access the linked list (you can't access the
# ImmutableListNode directly):
# ImmutableListNode.printValue(): Print value of the current node.
# ImmutableListNode.getNext(): Return the next node.


class Solution:
  def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    stack = []
    
    if not head:
      return

    while head:
      stack.append(head)
      head = head.getNext()

    while stack:
      node = stack.pop()
      node.printValue()
      
