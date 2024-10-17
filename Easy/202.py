# https://leetcode.com/problems/happy-number/description
# Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        for _ in range(50):
            no = sum(d**2 for d in digits)
            if no == 1:
                return True
            else:
                digits = [int(d) for d in str(no)]

              
# Using set
class Solution1:
    def isHappy(self, n: int) -> bool:
        no_set = set()
        while n != 1:
            if n in no_set:
                return False
            no_set.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        else:
            return True
    
