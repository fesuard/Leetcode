# https://leetcode.com/problems/self-dividing-numbers/description
# A self-dividing number is a number that is divisible by every digit it contains.
#   For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 
# and 128 % 8 == 0.
#   A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers
# in the range [left, right] (both inclusive).


# Brute force approach, we make a for loop from left to right + 1 and we check if
# each digit of the number is divisible to it by using a different for loop and 
# converting the number to a string.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for num in range(left, right + 1):
            digits = str(num)
            self_div = True

            for digit in digits:
                if digit == '0' or num % int(digit) != 0:
                    self_div = False
                    break
            
            if self_div:
                res.append(num)

        return res
      
