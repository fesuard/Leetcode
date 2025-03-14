# https://leetcode.com/problems/a-number-after-a-double-reversal/description
# Reversing an integer means to reverse all its digits.
# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading 
# zeros are not retained. Given an integer num, reverse num to get reversed1, then 
# reverse reversed1 to get reversed2. Return true if reversed2 equals num. 
# Otherwise return false.


# We turn the number into a string list, then check if it has at least 1 leading 0
# at the beginning and the end since it will be reversed, if so we return False
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        str_num = list(str(num))

        if str_num[0] == '0' or str_num[-1] == '0':
            return False
        
        return True
      
