# https://leetcode.com/problems/remove-trailing-zeros-from-a-string
# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.


# Since it is mentioned that num doesn't have any leading 0, we can just check starting from the end of num
# what is the last index that is not a zero, then we return through string slicing.
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1

        while num[i] == "0":
            i -= 1
        
        return num[ :i + 1]
        
