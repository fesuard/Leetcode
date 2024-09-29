#  You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in
#  the jth bank. Return the wealth that the richest customer has. A customer's wealth is the amount of money they
#  have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sorted_list = sorted(accounts, key=lambda x: sum(x), reverse=True)
        return sum(sorted_list[0])
