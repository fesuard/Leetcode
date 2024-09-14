https://leetcode.com/problems/roman-to-integer/description/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = dict()
        romans = ["I", "V", "X", "L", "C", "D", "M"]
        nums = [1, 5 ,10 ,50 ,100 ,500 ,1000]
        for i in range(len(romans)):
            roman_num[romans[i]] = nums[i]
        total = 0
        for i in range(len(s)):
            if i < len(s)-1 and roman_num[s[i+1]] > roman_num[s[i]]:
                total -= roman_num[s[i]]
            else:
                total += roman_num[s[i]]
        return total
        

