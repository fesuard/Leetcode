# https://leetcode.com/problems/sum-of-digits-in-base-k/description
# Given an integer n (in base 10) and a base k, return the sum of the digits of n 
# after converting n from base 10 to base k.After converting, each digit should be 
# interpreted as a base 10 number, and the sum should be returned in base 10.


# We calculate the number n in base k, and instead of storing the number, we just 
# add it's digits to res, since it's asking for the sum of the changed number.
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            res += n % k
            n //= k
        
        return res
