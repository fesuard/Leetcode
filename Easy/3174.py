# https://leetcode.com/problems/clear-digits/description
# You are given a string s. Your task is to remove all digits by doing this
# operation repeatedly:
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
# Note that the operation cannot be performed on a digit that does not have
# any non-digit character to its left.


# Using a stack
class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for char in s:
            if not char.isdigit():
                res.append(char)

            else:
                if res:
                    res.pop()

        return ''.join(res)


# Brute force approach
class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i].isdigit():
                j = i - 1

                while j >= 0 and s[j] == '':
                    j -= 1

                if j >= 0:
                    s[j] = ''

                s[i] = ''

        return ''.join(s)
        
