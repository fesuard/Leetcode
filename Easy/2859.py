# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
# Sum of Values at Indices With K Set Bits
# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set
# bits in their binary representation. The set bits in an integer are the 1's present when it is written
# in binary. For example, the binary representation of 21 is 10101, which has 3 set bits.
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                res.append(nums[i])
        return sum(res)
