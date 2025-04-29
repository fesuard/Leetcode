# https://leetcode.com/problems/sum-of-digits-in-base-k/description
# Given an integer n (in base 10) and a base k, return the sum of the digits of n 
# after converting n from base 10 to base k.After converting, each digit should be 
# interpreted as a base 10 number, and the sum should be returned in base 10.


# We calculate the number n in base k, store it in num. We iterate num and add its
# digits to the sum of res.
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num = ''
        while n > 0:
            num += str(n % k)
            n //= k
        
        res = 0
        for digit in num:
            res += int(digit)
        
        return res
