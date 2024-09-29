# https://leetcode.com/problems/split-with-minimum-sum/description/
# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
# The concatenation of num1 and num2 is a permutation of num. In other words, the sum of the number of
# occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros. Return the minimum possible sum of num1 and num2.


class Solution:
    def splitNum(self, num: int) -> int:
        n = ''.join(sorted(str(num)))
        return int(n[::2]) + int(n[1::2])
