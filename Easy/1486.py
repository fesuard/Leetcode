# https://leetcode.com/problems/xor-operation-in-an-array/description
# You are given an integer n and an integer start. Define an array nums where 
# nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0

        for _ in range(n):
            xor = xor ^ start
            start += 2

        return xor
      
