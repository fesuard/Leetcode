# https://leetcode.com/problems/harshad-number/description
# An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. 
# Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.


# Using type conversion
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        num_sum = sum(int(n) for n in str(x))

        if x % num_sum == 0:
            return num_sum
        
        return -1


# Without type conversion
class Solution1:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        sum_num = 0

        while temp > 0:
            sum_num += temp % 10
            temp //= 10

        if x % sum_num == 0:
            return sum_num

        return -1
      
