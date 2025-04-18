# https://leetcode.com/problems/baseball-game/description
# You are given a list of strings operations, where operations[i] is the ith operation you must apply
# to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for operation in operations:
            if operation == "+":
                res.append(sum(res[-2:]))
            
            elif operation == "D":
                res.append(res[-1] * 2)
            
            elif operation == "C":
                res.pop()
            
            else:
                res.append(int(operation))

        return sum(res)
      
