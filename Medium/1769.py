# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty,
# and '1' if it contains one ball. In one operation, you can move one ball from a box to an adjacent box. Box i is
# adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls
# to the ith box. Each answer[i] is calculated considering the initial state of the boxes.


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        valid_index = []
        n = len(boxes)

        for i, val in enumerate(boxes):
            if val == '1':
                valid_index.append(i)

        for i in range(n):
            moves = 0
            for elem in valid_index:
                if boxes[i] != elem:
                    moves += abs(i - elem)
            res.append(moves)

        return res
      
