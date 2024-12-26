# https://leetcode.com/problems/smallest-even-multiple/description
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        
        return n * 2
      
