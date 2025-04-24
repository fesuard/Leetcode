# https://leetcode.com/problems/strictly-palindromic-number/description
# An integer n is strictly palindromic if, for every base b between 2 and n - 2 
# (inclusive), the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.


# We create a helper function to convert an integer to a base. The helper function
# has 2 arguments, the number and the desired base. We iterate from 2 to n - 2 inclusive
# and we convert the number to the respective base until the converted number is not
# a palindrome, and we return False. If it passes the for loop, we return True.
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def integer_to_base(number, base):
            num = ""
            while number > 0:
               num += str(number % base)
               number //= base
            return num

        for base in range(2, n - 1): 
            int_to_base = integer_to_base(n, base)
            if int_to_base != int_to_base[::-1]:
                return False
        
        return True
      
