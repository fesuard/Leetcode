# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description
# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. 
# Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked
# in an additional time, making the list longer than usual. As the town detective, your task is to find
# these two sneaky numbers. Return an array of size two containing the two numbers (in any order).


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashm = {}
        res = []

        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1

        for key, value in hashm.items():
            if value == 2:
                res.append(key)

        return res
      
