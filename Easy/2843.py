# https://leetcode.com/problems/count-symmetric-integers/description
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n
# digits of x is equal to the sum of the last n digits of x. Numbers with an odd 
# number of digits are never symmetric. Return the number of symmetric integers 
# in the range [low, high].


# We use a brute force approach, first we convert the number into a string, and 
# we proceed with the rest if it's even. We iterate through the indexes of the 
# string until the half point, we add to balance if it's in the first half, and
# we subtract if it's in the second half. If balance is 0, we add 1 to res.
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for num in range(low, high + 1):
            string_num = str(num)
            n = len(string_num)

            if n % 2 == 0:
                balance = 0

                for i in range(n // 2):
                    balance += int(string_num[i])
                    balance -= int(string_num[n - i - 1])
                  
                
                if balance == 0:
                    res += 1
        
        return res
                
