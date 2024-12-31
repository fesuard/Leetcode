# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description
# Given an integer number n, return the difference between the product of its digits and the sum
# of its digits.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]

        prd = 1
        for d in digits:
            prd *= d

        return prd - sum(digits)    
        
