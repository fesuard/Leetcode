# https://leetcode.com/problems/to-lower-case/description
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.


# Using ord and chr functions
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []

        for char in s:
            if 65 <= ord(char) <= 90:
                char = chr(ord(char) + 32)
                res.append(char)
            else:
                res.append(char)

        return ''.join(res)


# Using lower function
class Solution1:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
      
