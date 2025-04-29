# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/description
# Given an integer n, return a string with n characters such that each character in such
# string occurs an odd number of times. The returned string must contain only lowercase 
# English letters. If there are multiples valid strings, return any of them.  


# Since it doesn't matter what letters we use, and we only have to take into account 
# the count of the letters, we will just add the letter frequency according to the
# parity of n.
class Solution:
    def generateTheString(self, n: int) -> str:
        res = []

        if n == 1:
            return 'a'

        else: 
            if n % 2 == 0:
                res = ['a'] * (n - 1)
                res.append('b')
            
            else:
                res = ['a'] * (n - 2)
                res.append('b')
                res.append('c')

        return ''.join(res)
