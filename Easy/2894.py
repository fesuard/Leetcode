# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description
# You are given positive integers n and m.
# Define two integers as follows:
# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_div = 0
        sum_not_div = 0
        
        for num in range(1, n + 1):
            if num % m != 0:
                sum_not_div += num
            
            else:
                sum_div += num

        return sum_not_div - sum_div
      
