# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description
# Hercy puts money in the Leetcode bank every day. He starts by putting in $1 on Monday, 
# the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day 
# before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in theLeetcode bank at the end 
# of the nth day.


# We continually add to res the current week + current day + 1, this way the weeks and 
# the days of the weekwill be properly tracked each week cycle.
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0

        for i in range(n):
            week = i // 7
            day = i % 7
            res += week + day + 1

        return res
