# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description
# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.


# iterative approach
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0

        for digit in str(num):
            if num % int(digit) == 0:
                res += 1

        return res


# using a generator
  class Solution1:
    def countDigits(self, num: int) -> int:
        return sum(num % int(digit) == 0 for digit in str(num))


# using a frequency hashmap so we don't repeat the same digit more than once
class Solution2:
    def countDigits(self, num: int) -> int:
        hmap = dict()
        res = 0

        for digit in str(num):
            hmap[digit] = hmap.get(digit, 0) + 1

        for digit in hmap:
            if num % int(digit) == 0:
                res += hmap[digit]

        return res
      
