# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
# Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        char_nums = []
        res = 0
        for num in nums:
            char_nums.append(str(num))
        for num in char_nums:
            if len(num) % 2 == 0:
                res += 1
        return res


# one liner:
class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])
