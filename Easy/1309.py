# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description
# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#   Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#   Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#   Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.


# We use 2 hashmaps(it could have worked with one, but I think the code is clearer with 2 separate ones), one for
# single digits, and one for double digits, we map the digits/number given to use to their proper characters,
# and with the final for we access the keys of the dictionary to get the needed characters so we can decrypt 
# the string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        single_digit = {'#': ''}
        double_digit = {}
        single = ord('a')
        double = ord('j')
        
        for i in range(1, 10):
            single_digit[f'{i}'] = chr(single)
            single += 1

        for i in range(10, 27):
            double_digit[f'{i}'] = chr(double)
            double += 1

        for i in range(len(s)):
            if i + 2 < len(s) and s[i + 2] == '#':
                res.append(double_digit[s[i : i + 2]])
            elif i + 1 < len(s) and s[i + 1] != '#':
                res.append(single_digit[s[i]])

        if s[-1] != '#':
            res.append(single_digit[s[-1]])

        return ''.join(res) 
