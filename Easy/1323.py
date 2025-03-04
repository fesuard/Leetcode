# https://leetcode.com/problems/maximum-69-number/description
# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 
# becomes 9, and 9 becomes 6).


class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        first = False

        for digit in str(num):
            if digit == '6' and first == False:
                digits.append('9')
                first = True

            else:
                digits.append(digit)

        return int(''.join(digits))
      
