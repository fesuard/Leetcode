# https://leetcode.com/problems/replace-all-digits-with-characters/description
# You are given a 0-indexed string s that has lowercase English letters in its even
# indices and digits in its odd indices. You must perform an operation shift(c, x), 
# where c is a character and x is a digit, that returns the xth character after c.
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will
# never exceed 'z'.


class Solution:
    def replaceDigits(self, s: str) -> str:
        s_lst = list(s)

        for i in range(1, len(s_lst), 2):
            s_lst[i] = chr(ord(s_lst[i - 1]) + int(s_lst[i]))

        return ''.join(s_lst)
      
